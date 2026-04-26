import os
import re

base_dir = r"c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\templates"

# 1. Update basic.html to use ai_bot.html instead of its hardcoded bot
basic_path = os.path.join(base_dir, 'basic.html')
with open(basic_path, 'r', encoding='utf-8') as f:
    basic_content = f.read()

# Replace <div id="ai-chat-wrapper" ... to </script> at the end with the include
basic_content = re.sub(
    r'<div id="ai-chat-wrapper".*?</script>', 
    "{% include 'ai_bot.html' %}", 
    basic_content, 
    flags=re.DOTALL
)

with open(basic_path, 'w', encoding='utf-8') as f:
    f.write(basic_content)
print("Updated basic.html to use {% include 'ai_bot.html' %}")

# 2. Update ai_bot.html with user-specific storage keys and immediate muting
ai_bot_path = os.path.join(base_dir, 'ai_bot.html')
with open(ai_bot_path, 'r', encoding='utf-8') as f:
    ai_bot = f.read()

script_patch = """
    const currentUser = "{% if user.is_authenticated %}{{ user.username|escapejs }}{% else %}guest{% endif %}";
    const historyKey = 'ai_chat_history_' + currentUser;
    const archiveKey = 'ai_chat_archive_' + currentUser;
    const voicePrefKey = 'ai_voice_pref_' + currentUser;

    let isVoiceEnabled = localStorage.getItem(voicePrefKey) !== 'false';

    // Set initial voice button state based on local storage
    if (!isVoiceEnabled) {
        voiceBtn.className = 'fas fa-volume-mute';
        voiceBtn.style.color = '#ff4d4d';
    } else {
        voiceBtn.className = 'fas fa-volume-up';
        voiceBtn.style.color = 'white';
    }

    function speakText(text) {
        if (!isVoiceEnabled) return;
        window.speechSynthesis.cancel();
        const cleanText = text.replace(/<\/?[^>]+(>|$)/g, ""); 
        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.rate = 1.0;
        window.speechSynthesis.speak(utterance);
    }

    function appendMessage(sender, text, id = null, save = true) {
        const bubble = document.createElement('div');
        if (id) bubble.id = id;
        const isAi = (sender === 'AI');
        
        bubble.style.cssText = `
            padding: 12px 16px; 
            border-radius: ${isAi ? '18px 18px 18px 4px' : '18px 18px 4px 18px'};
            align-self: ${isAi ? 'flex-start' : 'flex-end'};
            background: ${isAi ? '#ffffff' : 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)'};
            color: ${isAi ? '#1e293b' : 'white'};
            margin-bottom: 5px; max-width: 85%;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); font-size: 14px;
        `;
        
        if (isAi) {
            let parsedText = text;
            try { if (typeof marked !== 'undefined') parsedText = marked.parse(text); } catch(e) {}
            bubble.innerHTML = `<strong>AI Mentor:</strong> <div class="markdown-body">${parsedText}</div>`;
            setTimeout(() => { if (typeof Prism !== 'undefined') Prism.highlightAllUnder(bubble); }, 50);
            if (save) speakText(text);
        } else {
            bubble.innerHTML = `<strong>You:</strong><br>${text}`;
        }

        messagesContainer.appendChild(bubble);
        messagesContainer.scrollTo({ top: messagesContainer.scrollHeight, behavior: 'smooth' });

        if (save) {
            const history = JSON.parse(localStorage.getItem(historyKey) || '[]');
            history.push({ sender, text });
            localStorage.setItem(historyKey, JSON.stringify(history));
        }
    }

    clearBtn.onclick = function() {
        if(confirm("Are you sure you want to clear the chat history?")) {
            const currentHistory = localStorage.getItem(historyKey);
            let archive = JSON.parse(localStorage.getItem(archiveKey) || '[]');
            if(currentHistory) {
                archive.push({ timestamp: new Date().toLocaleString(), messages: JSON.parse(currentHistory) });
                localStorage.setItem(archiveKey, JSON.stringify(archive));
            }
            localStorage.removeItem(historyKey);
            messagesContainer.innerHTML = '';
            appendMessage('AI', 'History archived successfully! Chat screen cleared.', null, false);
        }
    };

    const saved = JSON.parse(localStorage.getItem(historyKey) || '[]');
    if(saved.length === 0) {
        appendMessage('AI', `Hello <strong>${currentUser}</strong>! Ready to start? 🚀`, null, false);
    } else {
        saved.forEach(msg => appendMessage(msg.sender, msg.text, null, false));
    }

    voiceBtn.onclick = function() {
        isVoiceEnabled = !isVoiceEnabled;
        this.className = isVoiceEnabled ? 'fas fa-volume-up' : 'fas fa-volume-mute';
        this.style.color = isVoiceEnabled ? 'white' : '#ff4d4d';
        localStorage.setItem(voicePrefKey, isVoiceEnabled);
        
        // Immediately stop talking if muted!
        if (!isVoiceEnabled) {
            window.speechSynthesis.cancel();
        }
    };
"""

# We'll replace the guts of the script
script_guts_pattern = re.compile(
    r'let isVoiceEnabled = true;.*?voiceBtn\.onclick = function\(\) {.*?};', 
    re.DOTALL
)

ai_bot = script_guts_pattern.sub(script_patch, ai_bot)

with open(ai_bot_path, 'w', encoding='utf-8') as f:
    f.write(ai_bot)
print("Updated ai_bot.html")
