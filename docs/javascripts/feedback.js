/* Page feedback — copied from ActianCorp/zeenea-platform-docs
 * (docs/javascripts/extra.js, "Page feedback" section).
 *
 * Sends the thumbs rating to GA4 as a `feedback` event, then offers an
 * optional free-text follow-up sent as `feedback_text`. The form itself is
 * rendered by the theme from extra.analytics.feedback in zensical.toml.
 */
window.document$.subscribe(function() {
    var feedback = document.forms.feedback;
    if (!feedback) return;
    feedback.hidden = false;
    feedback.addEventListener("submit", function(ev) {
        ev.preventDefault();
        var page = document.location.pathname;
        var data = ev.submitter.getAttribute("data-md-value");

        // Send initial rating event to GA4
        if (typeof gtag === "function") {
            gtag("event", "feedback", {
                page_path: page,
                rating: data
            });
        }

        // Disable rating buttons
        feedback.firstElementChild.disabled = true;

        // Hide any default thank-you notes
        var notes = feedback.querySelectorAll(".md-feedback__note [data-md-value]");
        for (var i = 0; i < notes.length; i++) notes[i].hidden = true;

        // Show text feedback form
        var existing = feedback.querySelector(".feedback-text-form");
        if (existing) existing.remove();

        var textForm = document.createElement("div");
        textForm.className = "feedback-text-form";
        textForm.innerHTML =
            '<p class="feedback-text-prompt">Want to tell us more? <span class="feedback-optional">(optional)</span></p>' +
            '<textarea class="feedback-textarea" maxlength="500" rows="3" placeholder="What can we improve on this page?"></textarea>' +
            '<div class="feedback-text-actions">' +
                '<button type="button" class="feedback-submit md-button md-button--primary">Submit</button>' +
                '<button type="button" class="feedback-skip">Skip</button>' +
            '</div>';
        feedback.appendChild(textForm);

        var textarea = textForm.querySelector(".feedback-textarea");
        var submitBtn = textForm.querySelector(".feedback-submit");
        var skipBtn = textForm.querySelector(".feedback-skip");

        function showThanks() {
            textForm.innerHTML = '<p class="feedback-thanks">Thanks for your feedback!</p>';
        }

        submitBtn.addEventListener("click", function() {
            var text = textarea.value.trim();
            if (text && typeof gtag === "function") {
                gtag("event", "feedback_text", {
                    page_path: page,
                    rating: data,
                    comment: text.substring(0, 500)
                });
            }
            showThanks();
        });

        skipBtn.addEventListener("click", showThanks);
    });
});
