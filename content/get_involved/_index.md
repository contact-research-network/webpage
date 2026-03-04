---
title: "Get Involved"
summary: "Join the Contact Research Network or subscribe to our newsletter."
date: 2025-11-09
type: "page"
markup: "html"
---
<style>
    .form-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .form-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    .form-label {
        font-weight: bold;
    }
    .form-textarea {
        resize: vertical;
        min-height: 110px;
    }
    .form-sublabel {
        font-size: 0.9em;
        color: #666;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .radio-group {
        display: flex;
        gap: 20px;
        margin-top: 5px;
    }
    .radio-option {
        display: flex;
        align-items: center;
        gap: 5px;
    }
</style>

<h2>Join the Network</h2>

Interested in joining the Contact Research Network? Fill out the form below to get involved!

<div class="form-container" style="width: 80%;">
    <form action="https://public.herotofu.com/v1/b49c9690-952e-11ef-a0ee-650b92707733" method="post" accept-charset="UTF-8" style="width: 75%;">
        <div class="form-group">
            <label for="name" class="form-label">Your Name</label>
            <input name="Name" id="name" type="text" required />
        </div>
        
        <div class="form-group">
            <label for="email" class="form-label">Your Email</label>
            <input name="Email" id="email" type="email" required />
        </div>
        
        <div class="form-group">
            <label for="position" class="form-label">Position</label>
            <input name="Position" id="position" type="text" required />
        </div>
        
        <div class="form-group">
            <label for="institution" class="form-label">Institution</label>
            <input name="Institution" id="institution" type="text" required />
        </div>
        
        <div class="form-group">
            <label for="orcid" class="form-label">ORCID</label>
            <input name="ORCID" id="orcid" type="text" required />
        </div>
        
        <div class="form-group">
            <label for="website" class="form-label">Link to personal website/LinkedIn to be included on our website (optional):</label>
            <input name="Website" id="website" type="url" />
        </div>
        
        <div class="form-group">
            <label class="form-label">Research Focus</label>
            <div class="form-sublabel">Have you conducted or are you currently conducting research related to intergroup contact or related topics?</div>
            <div class="radio-group">
                <div class="radio-option">
                    <input type="radio" id="research-yes" name="ResearchFocus" value="Yes" required onchange="toggleInterestField()" />
                    <label for="research-yes">Yes</label>
                </div>
                <div class="radio-option">
                    <input type="radio" id="research-no" name="ResearchFocus" value="No" required onchange="toggleInterestField()" />
                    <label for="research-no">No</label>
                </div>
            </div>
        </div>
        
        <div id="interest-field" class="form-group" style="display: none;">
            <label class="form-label" for="message">Your interest/expertise</label>
            <textarea class="form-textarea" name="Message" id="message"></textarea>
        </div>
        
        <div class="form-group">
            <label class="form-label">Photo Permission</label>
            <div class="form-sublabel">Do you give permission for us to use your photo from your university website on our members page?</div>
            <div class="radio-group">
                <div class="radio-option">
                    <input type="radio" id="photo-yes" name="PhotoPermission" value="Yes" required />
                    <label for="photo-yes">Yes</label>
                </div>
                <div class="radio-option">
                    <input type="radio" id="photo-no" name="PhotoPermission" value="No" required />
                    <label for="photo-no">No</label>
                </div>
            </div>
            <div class="form-sublabel">If you prefer to use a different photo, please email it to contactresearchnetwork@gmail.com</div>
        </div>
        
        <div class="form-group">
            <input type="submit" value="Request to join" />
            <div style="text-indent:-99999px; white-space:nowrap; overflow:hidden; position:absolute;" aria-hidden="true">
                <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" />
            </div>
        </div>
    </form>
</div>

<script>
function toggleInterestField() {
  const researchYes = document.getElementById("research-yes");
  const researchNo = document.getElementById("research-no");
  const interestField = document.getElementById("interest-field");
  const messageTextarea = document.getElementById("message");
  
  if (researchYes.checked) {
    interestField.style.display = "flex";
    messageTextarea.placeholder = "What was your latest research activity regarding intergroup contact?";
    messageTextarea.required = true;
  } else if (researchNo.checked) {
    interestField.style.display = "flex";
    messageTextarea.placeholder = "What was your latest research activity?";
    messageTextarea.required = true;
  } else {
    interestField.style.display = "none";
    messageTextarea.required = false;
  }
}
</script>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h2>Subscribe to Our Newsletter</h2>

<p>Stay up-to-date with the latest news and events by subscribing to our newsletter. <a href="https://contactresearch.substack.com/">Click here to subscribe</a>.</p>

<h2>Any other questions</h2>

<p>Please email one of the network convenors, or <a href="../#contact">send us a message here.</a></p>
