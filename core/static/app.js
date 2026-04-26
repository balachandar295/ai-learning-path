function showContent(type) {
    // 1. URL-la irundhu topic name-a edukkurom (e.g., simplification)
    const urlParams = new URLSearchParams(window.location.search);
    const topicKey = urlParams.get('topic') || 'simplification';

    // 2. data.js-la irundhu correct-ana topic data-va edukurom
    const data = topicsData[topicKey];

    if (data) {
        // 3. UI-a update panrom
        document.getElementById('side-topic-name').innerText = data.title;
        document.getElementById('content-title').innerText = type.charAt(0).toUpperCase() + type.slice(1);
        document.getElementById('content-body').innerHTML = data[type];
        
        // 4. Button colors-a active-ah mathurom
        const buttons = document.querySelectorAll('.tab-btn');
        buttons.forEach(btn => {
            btn.style.background = "white";
            btn.style.color = "black";
        });
        event.currentTarget.style.background = "#6c63ff";
        event.currentTarget.style.color = "white";
    }
}

// Page load aagum podhu default-ah explanation-a kaatanum
window.onload = () => {
    showContent('explanation');
};