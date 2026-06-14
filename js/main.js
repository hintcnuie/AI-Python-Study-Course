/* ========================================
   璐璐手作小屋 - 主脚本
   Lulu's Handmade Cottage - Main Script
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {

    // === Mobile Nav Toggle ===
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function() {
            navLinks.classList.toggle('show');
        });

        // Close nav when clicking a link
        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navLinks.classList.remove('show');
            });
        });

        // Close nav when clicking outside
        document.addEventListener('click', function(e) {
            if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('show');
            }
        });
    }

    // === Back to Top Button ===
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // === Active Nav Link ===
    const currentPath = window.location.pathname;
    const navAnchors = document.querySelectorAll('.nav-links a');
    navAnchors.forEach(function(link) {
        const href = link.getAttribute('href');
        if (href && currentPath.includes(href.replace(/\/$/, '').split('/').pop())) {
            link.classList.add('active');
        }
        // Home page special case
        if ((currentPath.endsWith('index.html') || currentPath.endsWith('/')) &&
            (href === 'index.html' || href === '../index.html')) {
            link.classList.add('active');
        }
    });

    // === Guestbook Form ===
    const guestbookForm = document.getElementById('guestbookForm');
    if (guestbookForm) {
        guestbookForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const name = document.getElementById('gName').value.trim();
            const email = document.getElementById('gEmail').value.trim();
            const content = document.getElementById('gContent').value.trim();

            if (!name || !content) {
                showToast('请填写昵称和留言内容哦~', 'error');
                return;
            }

            // Save to localStorage
            const messages = JSON.parse(localStorage.getItem('lulu_guestbook') || '[]');
            messages.unshift({
                name: name,
                email: email,
                content: content,
                time: new Date().toLocaleString('zh-CN'),
                reply: ''
            });
            localStorage.setItem('lulu_guestbook', JSON.stringify(messages));

            guestbookForm.reset();
            showToast('留言成功！感谢你的留言~', 'success');

            // Refresh message list if on same page
            if (document.getElementById('messageList')) {
                renderMessages();
            }
        });
    }

    // === Render Messages ===
    renderMessages();

    // === Contact Form ===
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('cName').value.trim();
            const content = document.getElementById('cContent').value.trim();
            if (!name || !content) {
                showToast('请填写姓名和内容哦~', 'error');
                return;
            }
            contactForm.reset();
            showToast('消息已发送！我会尽快回复~', 'success');
        });
    }

    // === Gallery Filter ===
    const filterBtns = document.querySelectorAll('.gallery-filter button');
    const galleryItems = document.querySelectorAll('.gallery-item');
    if (filterBtns.length && galleryItems.length) {
        filterBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                filterBtns.forEach(function(b) { b.classList.remove('active'); });
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');
                galleryItems.forEach(function(item) {
                    if (filter === 'all' || item.getAttribute('data-category') === filter) {
                        item.style.display = '';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // === Link Exchange Form ===
    const linkForm = document.getElementById('linkForm');
    if (linkForm) {
        linkForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const siteName = document.getElementById('lName').value.trim();
            const siteUrl = document.getElementById('lUrl').value.trim();
            if (!siteName || !siteUrl) {
                showToast('请填写网站名称和网址~', 'error');
                return;
            }
            linkForm.reset();
            showToast('友链申请已提交，审核通过后会添加哦~', 'success');
        });
    }

    // === Newsletter ===
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('nEmail').value.trim();
            if (!email) {
                showToast('请输入邮箱地址~', 'error');
                return;
            }
            newsletterForm.reset();
            showToast('订阅成功！感谢关注~', 'success');
        });
    }

});

// === Render Messages from localStorage ===
function renderMessages() {
    const container = document.getElementById('messageList');
    if (!container) return;

    const messages = JSON.parse(localStorage.getItem('lulu_guestbook') || '[]');

    if (messages.length === 0) {
        container.innerHTML = '<div style="text-align:center;padding:40px;color:#A89888;">还没有留言，快来坐沙发吧~ 🛋️</div>';
        return;
    }

    container.innerHTML = messages.map(function(msg) {
        return '<div class="message-item">' +
            '<div class="msg-header">' +
                '<span class="msg-author">' + escapeHtml(msg.name) + '</span>' +
                '<span class="msg-time">' + escapeHtml(msg.time) + '</span>' +
            '</div>' +
            '<div class="msg-content">' + escapeHtml(msg.content) + '</div>' +
            (msg.reply ? '<div class="msg-reply"><strong>博主回复：</strong>' + escapeHtml(msg.reply) + '</div>' : '') +
        '</div>';
    }).join('');
}

// === Toast Message ===
function showToast(msg, type) {
    // Remove existing toast
    const existing = document.querySelector('.msg-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'msg-toast ' + (type || 'success');
    toast.textContent = msg;
    document.body.appendChild(toast);

    setTimeout(function() {
        if (toast.parentNode) toast.remove();
    }, 3000);
}

// === Escape HTML ===
function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
}

// ========================================
//   Background Music Player (Web Audio API)
//   Cheerful, light ambient — major-key chimes
// ========================================
(function() {
    var audioCtx = null;
    var masterGain = null;
    var isPlaying = false;
    var noteTimer = null;
    var toggleBtn = null;

    // C-major scale across two octaves (C5-C7), bright and cheerful
    var majorScale = [
        523.25,  // C5
        587.33,  // D5
        659.25,  // E5
        698.46,  // F5
        783.99,  // G5
        880.00,  // A5
        987.77,  // B5
        1046.50, // C6
        1174.66, // D6
        1318.51, // E6
        1396.91, // F6
        1567.98, // G6
        1760.00, // A6
        1975.53, // B6
        2093.00  // C7
    ];

    // Happy-sounding ascending patterns (indices into majorScale)
    var miniMelodies = [
        [0, 2, 4, 7],         // C-E-G-C  (major arpeggio)
        [1, 3, 5, 8],         // D-F-A-D
        [3, 5, 7, 10],        // F-A-C-F
        [2, 4, 6, 9],         // E-G-B-E
        [4, 7, 9, 12],        // G-C-E-G
        [0, 2, 4],            // C-E-G
        [5, 7, 9],            // A-C-E
        [7, 9, 12, 14],       // C-E-G-C (high)
        [0, 4, 7],            // C-G-C  (open fifth)
        [5, 9, 12],           // A-E-C
    ];

    function initAudio() {
        if (audioCtx) return;
        try {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            masterGain = audioCtx.createGain();
            masterGain.gain.value = 0.10; // Gentle background level
            masterGain.connect(audioCtx.destination);
        } catch (e) {
            console.log('Web Audio API not supported');
        }
    }

    // Create a single note with the given frequency and timing
    function scheduleTone(freq, startTime, duration, velocity) {
        if (!audioCtx) return;

        // Triangle wave — warm but bright, cheerful timbre
        var osc = audioCtx.createOscillator();
        osc.type = 'triangle';
        osc.frequency.value = freq;
        osc.detune.value = (Math.random() - 0.5) * 8;

        var noteGain = audioCtx.createGain();
        var peak = velocity * 0.25;
        noteGain.gain.setValueAtTime(0, startTime);
        noteGain.gain.linearRampToValueAtTime(peak, startTime + 0.08);
        noteGain.gain.setValueAtTime(peak * 0.7, startTime + duration * 0.4);
        noteGain.gain.linearRampToValueAtTime(0, startTime + duration);

        osc.connect(noteGain);
        noteGain.connect(masterGain);

        osc.start(startTime);
        osc.stop(startTime + duration + 0.1);
    }

    // Add a sparkly overtone an octave above (very quiet)
    function scheduleSparkle(freq, startTime, duration, velocity) {
        if (!audioCtx) return;

        var osc = audioCtx.createOscillator();
        osc.type = 'sine';
        osc.frequency.value = freq * 2; // One octave up
        osc.detune.value = 3 + Math.random() * 5;

        var noteGain = audioCtx.createGain();
        var peak = velocity * 0.06;
        noteGain.gain.setValueAtTime(0, startTime);
        noteGain.gain.linearRampToValueAtTime(peak, startTime + 0.06);
        noteGain.gain.linearRampToValueAtTime(0, startTime + duration * 0.6);

        osc.connect(noteGain);
        noteGain.connect(masterGain);

        osc.start(startTime);
        osc.stop(startTime + duration * 0.6 + 0.1);
    }

    function playPhrase() {
        if (!audioCtx || !isPlaying) return;

        var now = audioCtx.currentTime;
        var roll = Math.random();

        if (roll < 0.35) {
            // —— Play a short ascending mini-melody (cheerful) ——
            var melody = miniMelodies[Math.floor(Math.random() * miniMelodies.length)];
            var gap = 0.28 + Math.random() * 0.2; // Light, bouncy spacing
            var noteDuration = gap * 1.4;

            for (var i = 0; i < melody.length; i++) {
                var freq = majorScale[melody[i]];
                var t = now + i * gap;
                var vel = 0.7 + i * 0.1; // Slightly crescendo through the phrase
                scheduleTone(freq, t, noteDuration, vel);
                scheduleSparkle(freq, t, noteDuration, vel);
            }

            // Pause after phrase
            var phraseLength = melody.length * gap;
            var nextDelay = phraseLength + 800 + Math.random() * 1800;
            noteTimer = setTimeout(playPhrase, nextDelay);

        } else if (roll < 0.55) {
            // —— Two-note chord (thirds or fifths sound happy) ——
            var idx = Math.floor(Math.random() * (majorScale.length - 4));
            var f1 = majorScale[idx];
            // Pick a third (index+2) or fifth (index+4) above
            var f2 = majorScale[Math.random() < 0.6 ? idx + 2 : idx + 4];

            var dur = 1.2 + Math.random() * 0.6;
            scheduleTone(f1, now, dur, 0.7);
            scheduleSparkle(f1, now, dur, 0.7);
            scheduleTone(f2, now, dur, 0.55);
            scheduleSparkle(f2, now, dur, 0.55);

            var nextDelay = dur + 600 + Math.random() * 1400;
            noteTimer = setTimeout(playPhrase, nextDelay);

        } else {
            // —— Single cheerful note ——
            var freq = majorScale[Math.floor(Math.random() * majorScale.length)];
            var dur = 0.9 + Math.random() * 0.8;
            scheduleTone(freq, now, dur, 0.85);
            scheduleSparkle(freq, now, dur, 0.85);

            var nextDelay = dur + 400 + Math.random() * 1000;
            noteTimer = setTimeout(playPhrase, nextDelay);
        }
    }

    function startMusic() {
        if (isPlaying) return;
        initAudio();

        if (audioCtx && audioCtx.state === 'suspended') {
            audioCtx.resume().then(function() {
                isPlaying = true;
                playPhrase();
                updateToggleState();
            });
        } else if (audioCtx) {
            isPlaying = true;
            playPhrase();
            updateToggleState();
        }
    }

    function stopMusic() {
        isPlaying = false;
        if (noteTimer) {
            clearTimeout(noteTimer);
            noteTimer = null;
        }
        updateToggleState();
    }

    function toggleMusic() {
        if (isPlaying) {
            stopMusic();
            try { localStorage.setItem('lulu_music', 'off'); } catch(e) {}
        } else {
            startMusic();
            try { localStorage.setItem('lulu_music', 'on'); } catch(e) {}
        }
    }

    function updateToggleState() {
        if (!toggleBtn) return;
        if (isPlaying) {
            toggleBtn.classList.add('playing');
            toggleBtn.setAttribute('aria-label', '暂停背景音乐');
            toggleBtn.setAttribute('title', '暂停音乐');
            toggleBtn.textContent = '🎵';
        } else {
            toggleBtn.classList.remove('playing');
            toggleBtn.setAttribute('aria-label', '播放背景音乐');
            toggleBtn.setAttribute('title', '播放音乐');
            toggleBtn.textContent = '🎶';
        }
    }

    function createToggleButton() {
        toggleBtn = document.createElement('button');
        toggleBtn.className = 'music-toggle';
        toggleBtn.setAttribute('aria-label', '播放背景音乐');
        toggleBtn.setAttribute('title', '播放音乐');
        toggleBtn.textContent = '🎶';
        toggleBtn.addEventListener('click', toggleMusic);
        document.body.appendChild(toggleBtn);

        try {
            if (localStorage.getItem('lulu_music') === 'on') {
                startMusic();
            }
        } catch(e) {}
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createToggleButton);
    } else {
        createToggleButton();
    }
})();
