import re

with open('core/templates/jobs.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_script = '''<script>
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.getElementById('jobForm');
            const feed = document.getElementById('jobsFeed');

            let storedJobs = JSON.parse(localStorage.getItem('ai_jobs_board') || '[]');

            function createJobCard(job) {
                let typeClass = 'fulltime';
                if (job.type && job.type.toLowerCase().includes('intern')) typeClass = 'internship';

                const platformBadge = job.platform 
                    ? `<span class="badge" style="background: #e2e8f0; color: #334155;"><i class="fas fa-globe"></i> ${job.platform}</span>` 
                    : '<span class="badge"><i class="fas fa-bolt"></i> User Posted</span>';

                return `
                    <div class="job-card">
                        <div class="job-header">
                            <div>
                                <h3 class="job-title">${job.title}</h3>
                                <p class="job-company">${job.company}</p>
                            </div>
                            <span style="font-size:0.8rem; color: #94a3b8;"><i class="fas fa-clock"></i> ${job.date}</span>
                        </div>
                        <div class="job-badges">
                            <span class="badge ${typeClass}">${job.type}</span>
                            ${platformBadge}
                        </div>
                        <p class="job-desc">${job.desc}</p>
                        <a href="${job.link}" target="_blank" class="apply-btn">Apply Now <i class="fas fa-arrow-right" style="margin-left: 5px;"></i></a>
                    </div>
                `;
            }

            async function loadJobs() {
                feed.innerHTML = '<p style="padding:20px; color:#64748b; font-weight:600;"><i class="fas fa-spinner fa-spin"></i> Automatically updating latest opportunities from Naukri, Indeed, and Internshala...</p>';
                let apiJobs = [];
                try {
                    const res = await fetch('/api/jobs/');
                    if(res.ok) {
                        const data = await res.json();
                        apiJobs = data.jobs || [];
                    }
                } catch(e) {
                    console.error('Error fetching API jobs', e);
                }
                
                const allJobs = [...apiJobs, ...storedJobs];
                feed.innerHTML = '';
                
                if(allJobs.length === 0) {
                    feed.innerHTML = '<p>No jobs available right now.</p>';
                    return;
                }
                
                allJobs.reverse().forEach(job => {
                    feed.insertAdjacentHTML('beforeend', createJobCard(job));
                });
            }

            loadJobs();

            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const newJob = {
                    title: document.getElementById('jobTitle').value,
                    company: document.getElementById('jobCompany').value,
                    type: document.getElementById('jobType').value,
                    desc: document.getElementById('jobDesc').value,
                    link: document.getElementById('jobLink').value,
                    date: new Date().toLocaleDateString()
                };
                storedJobs.push(newJob);
                localStorage.setItem('ai_jobs_board', JSON.stringify(storedJobs));
                
                loadJobs();
                form.reset();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        });
    </script>'''

content = re.sub(r'<script>.*?</script>', new_script, content, flags=re.DOTALL)

with open('core/templates/jobs.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
