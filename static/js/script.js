// Skyfall Sound & Light — Audio Visual Client Architecture

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initBookingWizard();
  initInteractiveQuoteCalculator();
  initTechFeatureFilter();
  initNewsletterAJAX();
  initAudioVisualSim();
  initSmashBalloonFeed();
});

/* -------------------------------------------------------------
 * 1. Mobile Menu Drawer
 * ------------------------------------------------------------- */
function initMobileMenu() {
  const drawer = document.getElementById('mobileMenuDrawer');
  const openBtn = document.getElementById('openMobileMenuBtn');
  const closeBtn = document.getElementById('closeMobileMenuBtn');
  const navLinks = document.querySelectorAll('.mobile-nav-link');
  const mobileBookingBtn = document.getElementById('mobileBookingBtn');

  if (!drawer || !openBtn || !closeBtn) return;

  function openMenu() {
    drawer.classList.add('mobile-menu-active');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    drawer.classList.remove('mobile-menu-active');
    document.body.style.overflow = '';
  }

  openBtn.addEventListener('click', openMenu);
  closeBtn.addEventListener('click', closeMenu);

  navLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  if (mobileBookingBtn) {
    mobileBookingBtn.addEventListener('click', () => {
      closeMenu();
      openBookingModal();
    });
  }
}

/* -------------------------------------------------------------
 * 2. Multi-Step Event Quote & Booking Modal Wizard
 * ------------------------------------------------------------- */
let currentStep = 1;

function openBookingModal(presetEventType = null) {
  const modal = document.getElementById('bookingModal');
  if (!modal) return;
  modal.classList.add('modal-active');
  document.body.style.overflow = 'hidden';

  if (presetEventType) {
    const inputEventType = document.getElementById('inputEventType');
    if (inputEventType) inputEventType.value = presetEventType;
  }
}

function closeBookingModal() {
  const modal = document.getElementById('bookingModal');
  if (!modal) return;
  modal.classList.remove('modal-active');
  document.body.style.overflow = '';
}

function initBookingWizard() {
  const backdrop = document.getElementById('bookingBackdrop');
  const closeBtn = document.getElementById('closeBookingBtn');
  const nextBtn = document.getElementById('wizardNextBtn');
  const backBtn = document.getElementById('wizardBackBtn');
  const closeSuccessBtn = document.getElementById('closeSuccessBtn');
  const wizardForm = document.getElementById('bookingWizardForm');

  const bookingTriggers = [
    'openBookingBtn',
    'heroBookingBtn',
    'stickyBookingBtn',
    'techBookingBtn',
    'footerBookingBtn',
    'contactBookingBtn'
  ];

  bookingTriggers.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('click', () => openBookingModal());
  });

  if (closeBtn) closeBtn.addEventListener('click', closeBookingModal);
  if (backdrop) backdrop.addEventListener('click', closeBookingModal);
  if (closeSuccessBtn) closeSuccessBtn.addEventListener('click', closeBookingModal);

  // Step 1: Event Type Selection
  const eventOptions = document.querySelectorAll('.event-type-option');
  const inputEventType = document.getElementById('inputEventType');
  eventOptions.forEach(btn => {
    btn.addEventListener('click', () => {
      eventOptions.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (inputEventType) inputEventType.value = btn.dataset.value;
      updateNextButtonState();
    });
  });

  // Step 2: Guest Count Selection
  const guestOptions = document.querySelectorAll('.guest-option');
  const inputGuestCount = document.getElementById('inputGuestCount');
  guestOptions.forEach(btn => {
    btn.addEventListener('click', () => {
      guestOptions.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (inputGuestCount) inputGuestCount.value = btn.dataset.value;
      updateNextButtonState();
    });
  });

  // Step 3 Inputs Validation & Services Checklist
  const serviceCheckboxes = document.querySelectorAll('.service-checkbox');
  const inputServicesNeeded = document.getElementById('inputServicesNeeded');
  serviceCheckboxes.forEach(cb => {
    cb.addEventListener('change', () => {
      const selected = Array.from(serviceCheckboxes)
        .filter(c => c.checked)
        .map(c => c.value);
      if (inputServicesNeeded) inputServicesNeeded.value = selected.join(', ');
    });
  });

  // Step 4 Inputs Validation
  const inputName = document.getElementById('inputName');
  const inputEmail = document.getElementById('inputEmail');
  const inputPhone = document.getElementById('inputPhone');

  [inputName, inputEmail, inputPhone].forEach(input => {
    if (input) {
      input.addEventListener('input', updateNextButtonState);
    }
  });

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentStep < 4) {
        setStep(currentStep + 1);
      } else if (currentStep === 4) {
        submitWizardForm();
      }
    });
  }

  if (backBtn) {
    backBtn.addEventListener('click', () => {
      if (currentStep > 1) {
        setStep(currentStep - 1);
      }
    });
  }

  function setStep(step) {
    currentStep = step;
    for (let i = 1; i <= 4; i++) {
      const stepEl = document.getElementById(`wizardStep${i}`);
      const badgeEl = document.getElementById(`stepBadge${i}`);
      const labelEl = document.getElementById(`stepLabel${i}`);

      if (stepEl) {
        if (i === step) {
          stepEl.classList.remove('hidden');
        } else {
          stepEl.classList.add('hidden');
        }
      }

      if (badgeEl && labelEl) {
        if (i <= step) {
          badgeEl.classList.remove('bg-muted/30', 'text-muted-foreground');
          badgeEl.classList.add('bg-primary', 'text-primary-foreground');
          labelEl.classList.remove('text-muted-foreground');
          labelEl.classList.add('text-foreground');
        } else {
          badgeEl.classList.remove('bg-primary', 'text-primary-foreground');
          badgeEl.classList.add('bg-muted/30', 'text-muted-foreground');
          labelEl.classList.remove('text-foreground');
          labelEl.classList.add('text-muted-foreground');
        }
      }
    }

    if (backBtn) {
      if (step > 1) {
        backBtn.classList.remove('hidden');
      } else {
        backBtn.classList.add('hidden');
      }
    }

    if (nextBtn) {
      const btnSpan = nextBtn.querySelector('span');
      if (btnSpan) {
        btnSpan.textContent = step === 4 ? 'Request Quote' : 'Continue';
      }
    }

    updateNextButtonState();
  }

  function updateNextButtonState() {
    if (!nextBtn) return;

    let valid = true;
    if (currentStep === 1) {
      valid = !!inputEventType && !!inputEventType.value;
    } else if (currentStep === 2) {
      valid = !!inputGuestCount && !!inputGuestCount.value;
    } else if (currentStep === 4) {
      valid = !!(inputName && inputName.value.trim()) &&
              !!(inputEmail && inputEmail.value.trim()) &&
              !!(inputPhone && inputPhone.value.trim());
    }

    nextBtn.disabled = !valid;
    if (valid) {
      nextBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    } else {
      nextBtn.classList.add('opacity-50', 'cursor-not-allowed');
    }
  }

  function submitWizardForm() {
    if (!wizardForm) return;
    const formData = new FormData(wizardForm);
    const json = {};
    formData.forEach((val, key) => json[key] = val);

    nextBtn.disabled = true;
    nextBtn.innerHTML = 'Submitting...';

    fetch('/api/book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(json)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        const wizardBody = document.getElementById('wizardBody');
        const wizardSuccess = document.getElementById('wizardSuccess');
        const successMsg = document.getElementById('successMsg');

        if (wizardBody) wizardBody.classList.add('hidden');
        if (wizardSuccess) wizardSuccess.classList.remove('hidden');
        if (successMsg) successMsg.textContent = data.message;
      } else {
        alert(data.error || 'Submission failed. Please try again.');
      }
    })
    .catch(err => {
      console.error(err);
      alert('An error occurred. Please call +27 81 718 1206 for immediate assistance.');
    })
    .finally(() => {
      nextBtn.disabled = false;
      nextBtn.innerHTML = '<span>Request Quote</span>';
    });
  }
}

/* -------------------------------------------------------------
 * 3. Interactive Instant Quote & Package Estimator
 * ------------------------------------------------------------- */
function initInteractiveQuoteCalculator() {
  const calcForm = document.getElementById('quoteCalcForm');
  if (!calcForm) return;

  const eventTypeSelect = document.getElementById('calcEventType');
  const guestSlider = document.getElementById('calcGuestSlider');
  const guestDisplay = document.getElementById('calcGuestDisplay');
  const soundTierSelect = document.getElementById('calcSoundTier');
  const lightingTierSelect = document.getElementById('calcLightingTier');
  const fxCheckboxes = document.querySelectorAll('.calc-fx-checkbox');
  const priceDisplay = document.getElementById('calcPriceDisplay');
  const summaryDisplay = document.getElementById('calcSummaryDisplay');

  function updateCalculation() {
    if (!guestSlider || !priceDisplay) return;

    const guests = guestSlider.value;
    if (guestDisplay) guestDisplay.textContent = `${guests} Guests`;

    const selectedFX = Array.from(fxCheckboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    const payload = {
      event_type: eventTypeSelect ? eventTypeSelect.value : 'wedding',
      guest_count: parseInt(guests),
      sound_tier: soundTierSelect ? soundTierSelect.value : 'standard',
      lighting_tier: lightingTierSelect ? lightingTierSelect.value : 'standard',
      fx_items: selectedFX
    };

    fetch('/api/quote-calculator', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        priceDisplay.textContent = `${data.estimated_min} – ${data.estimated_max}`;
        if (summaryDisplay) summaryDisplay.textContent = data.summary;
      }
    })
    .catch(err => console.error(err));
  }

  if (guestSlider) guestSlider.addEventListener('input', updateCalculation);
  if (eventTypeSelect) eventTypeSelect.addEventListener('change', updateCalculation);
  if (soundTierSelect) soundTierSelect.addEventListener('change', updateCalculation);
  if (lightingTierSelect) lightingTierSelect.addEventListener('change', updateCalculation);
  fxCheckboxes.forEach(cb => cb.addEventListener('change', updateCalculation));

  // Run initial calculation
  updateCalculation();
}

/* -------------------------------------------------------------
 * 4. Equipment & Category Filters
 * ------------------------------------------------------------- */
function initTechFeatureFilter() {
  const filterBtns = document.querySelectorAll('.tech-filter-btn');
  const techCards = document.querySelectorAll('.tech-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const category = btn.dataset.category;

      filterBtns.forEach(b => {
        b.classList.remove('bg-primary', 'text-primary-foreground');
        b.classList.add('glass-cyber', 'text-foreground/70');
      });
      btn.classList.remove('glass-cyber', 'text-foreground/70');
      btn.classList.add('bg-primary', 'text-primary-foreground');

      techCards.forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
}

/* -------------------------------------------------------------
 * 5. Newsletter Form AJAX
 * ------------------------------------------------------------- */
function initNewsletterAJAX() {
  const newsForm = document.getElementById('newsletterForm');
  if (!newsForm) return;

  newsForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const emailInput = newsForm.querySelector('input[type="email"]');
    if (!emailInput || !emailInput.value) return;

    fetch('/api/newsletter', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: emailInput.value })
    })
    .then(res => res.json())
    .then(data => {
      alert(data.message);
      emailInput.value = '';
    })
    .catch(err => console.error(err));
  });
}

/* -------------------------------------------------------------
 * 6. Audio Visualizer Random Pulse Simulator
 * ------------------------------------------------------------- */
function initAudioVisualSim() {
  const eqBars = document.querySelectorAll('.eq-bar');
  if (!eqBars.length) return;

  setInterval(() => {
    eqBars.forEach(bar => {
      const randomHeight = Math.floor(Math.random() * 85) + 15;
      bar.style.height = `${randomHeight}%`;
    });
  }, 400);
}

/* -------------------------------------------------------------
 * 7. Smash Balloon Social Feed Recreation
 * ------------------------------------------------------------- */
function initSmashBalloonFeed() {
  const feedContainer = document.getElementById('smashBalloonGrid');
  const platformTabs = document.querySelectorAll('.sb-tab-btn');
  const lightboxModal = document.getElementById('smashLightboxModal');
  const closeLightboxBtn = document.getElementById('closeSmashLightboxBtn');
  const backdropLightbox = document.getElementById('smashLightboxBackdrop');

  if (!feedContainer) return;

  // Delegate click events on post cards to open Lightbox
  document.addEventListener('click', (e) => {
    const card = e.target.closest('.sb-post-card');
    if (card) {
      const postData = {
        title: card.dataset.title,
        caption: card.dataset.caption,
        image: card.dataset.image,
        platform: card.dataset.platform,
        handle: card.dataset.handle,
        author: card.dataset.author,
        avatar: card.dataset.avatar,
        likes: card.dataset.likes,
        comments: card.dataset.comments,
        timestamp: card.dataset.timestamp,
        url: card.dataset.url
      };
      openSmashLightbox(postData);
    }
  });

  if (closeLightboxBtn) closeLightboxBtn.addEventListener('click', closeSmashLightbox);
  if (backdropLightbox) backdropLightbox.addEventListener('click', closeSmashLightbox);

  // Platform Filter Tab switching via AJAX
  platformTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const platform = tab.dataset.platform;

      platformTabs.forEach(t => {
        t.classList.remove('bg-primary', 'text-background', 'font-bold');
        t.classList.add('glass-cyber', 'text-foreground/70');
      });
      tab.classList.remove('glass-cyber', 'text-foreground/70');
      tab.classList.add('bg-primary', 'text-background', 'font-bold');

      fetch(`/api/social-feed?platform=${platform}`)
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            renderFeedGrid(data.posts);
          }
        })
        .catch(err => console.error(err));
    });
  });

  function renderFeedGrid(posts) {
    feedContainer.innerHTML = '';
    posts.forEach(post => {
      const isInsta = post.platform === 'instagram';
      const isFb = post.platform === 'facebook';
      const badgeClass = isInsta ? 'smash-balloon-badge-instagram' : (isFb ? 'smash-balloon-badge-facebook' : 'smash-balloon-badge-tiktok');
      const platformLabel = isInsta ? 'Instagram' : (isFb ? 'Facebook' : 'TikTok');

      const cardHtml = `
        <div class="sb-post-card group"
             data-title="${escapeHtml(post.title)}"
             data-caption="${escapeHtml(post.caption)}"
             data-image="${post.image}"
             data-platform="${post.platform}"
             data-handle="${post.handle}"
             data-author="${escapeHtml(post.author_name)}"
             data-avatar="${post.avatar}"
             data-likes="${post.likes}"
             data-comments="${post.comments}"
             data-timestamp="${post.timestamp}"
             data-url="${post.url}">
          <div class="aspect-square relative overflow-hidden">
            <img src="${post.image}" alt="${escapeHtml(post.title)}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
            <div class="absolute top-3 left-3">
              <span class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full ${badgeClass}">${platformLabel}</span>
            </div>
            
            <div class="sb-post-overlay">
              <div class="flex items-center gap-2">
                <div class="w-7 h-7 rounded-full overflow-hidden bg-white/20">
                  <img src="${post.avatar}" class="w-full h-full object-cover">
                </div>
                <span class="text-xs font-bold text-white">${post.handle}</span>
              </div>
              <p class="text-xs text-white/90 line-clamp-3 leading-relaxed">${escapeHtml(post.caption)}</p>
              <div class="flex items-center justify-between text-xs text-primary font-bold">
                <span>❤️ ${post.likes}</span>
                <span>💬 ${post.comments}</span>
                <span class="text-[10px] text-white/60">${post.timestamp}</span>
              </div>
            </div>
          </div>
        </div>
      `;
      feedContainer.insertAdjacentHTML('beforeend', cardHtml);
    });
  }

  function openSmashLightbox(post) {
    if (!lightboxModal) return;

    document.getElementById('sbLbAvatar').src = post.avatar;
    document.getElementById('sbLbAuthor').textContent = post.author;
    document.getElementById('sbLbHandle').textContent = post.handle;
    document.getElementById('sbLbImage').src = post.image;
    document.getElementById('sbLbCaption').textContent = post.caption;
    document.getElementById('sbLbLikes').textContent = post.likes;
    document.getElementById('sbLbComments').textContent = post.comments;
    document.getElementById('sbLbTimestamp').textContent = post.timestamp;
    
    const linkBtn = document.getElementById('sbLbLink');
    if (linkBtn) {
      linkBtn.href = post.url;
      linkBtn.textContent = `View on ${post.platform.toUpperCase()}`;
    }

    lightboxModal.classList.add('modal-active');
    document.body.style.overflow = 'hidden';
  }

  function closeSmashLightbox() {
    if (!lightboxModal) return;
    lightboxModal.classList.remove('modal-active');
    document.body.style.overflow = '';
  }

  function escapeHtml(text) {
    if (!text) return '';
    return text.replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
}
