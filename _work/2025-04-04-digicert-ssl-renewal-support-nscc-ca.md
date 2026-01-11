---
title: "DigiCert SSL Certificate Renewal: support.nscc.ca"
date: 2025-04-04
categories: [work, it-management, ssl-certificates]
tags: [nscc, digicert, certificate-renewal, infrastructure]
context: Chat transcript documenting SSL certificate renewal process
---

# DigiCert SSL Certificate Renewal: support.nscc.ca

**Date:** April 4, 2025  
**Certificate:** support.nscc.ca  
**Agent:** Mandy (DigiCert Support)  
**Issue:** Certificate renewal with outdated contact information

## Context

I initiated the renewal of the SSL certificate for support.nscc.ca but encountered verification challenges due to outdated contact information in DigiCert's records. As the listed Point of Contact (POC), I was no longer in that specific role, and the existing verification phone number and email addresses were either unmonitored or routed to general switchboards.

## Resolution Process

### Initial Challenge
- **Verification phone number:** +19024916722 (general switchboard, not suitable for verification)
- **Email address on file:** ITcampus.info@nscc.ca (unmonitored campus inbox)

### Solution
I identified an appropriate contact who was:
- Listed in NSCC's public employee directory
- In the appropriate role (IT Infrastructure Manager)
- Available to receive and respond to verification emails

**Selected contact:** Andre Klefenz (andre.klefenz@nscc.ca)

### Verification Status
- **Domain validation:** nscc.ca already validated (March 7, 2025)
- **Valid for EV until:** April 8, 2026
- **Valid for OV until:** April 8, 2026
- **DCV Method:** Email (webmaster@nscc.ca)

## Key Takeaways

1. **Keep contact information current** in certificate authority records
2. **Use publicly verifiable contacts** listed in employee directories
3. **Domain validation remains valid** for 12+ months once completed
4. **Email verification** is more reliable than phone for institutional certificates
5. **Alternative verification methods** available: postal letter or legal opinion letter

## Chat Transcript

**Mandy (12:57:25 PM):** Thanks for using DigiCert Live Chat! You are now chatting with Mandy.

**Mandy (12:57:47 PM):** Good day Doug I hope you are well

**Me (12:57:53 PM):** I am!

**Me (12:58:55 PM):** I need to renew the cert for support.nscc.ca. I'm listed as the POC, but am no longer in that role)

**Mandy (12:59:29 PM):** I see the verification call is pending for Nova Scotia Community College

**Mandy (1:00:16 PM):** We have verified the number +19024916722 is anyone available to accept the call if we attempt the call now?

**Me (1:00:29 PM):** just a sec.

**Me (1:01:29 PM):** I'm not sure that is an active number.. stand by

**Mandy (1:01:52 PM):** Certainly

**Me (1:04:26 PM):** so that's a switchboard to any number of different people. Is there another way to verify?

**Mandy (1:07:15 PM):** We can also validate via email I have verified the following email address please can you advice if you are able to access the email ITcampus.info@nscc.ca

**Me (1:08:20 PM):** no... That's an unmonitored inbox for one of our campuses

**Mandy (1:08:59 PM):** Can you advise if there is an email address on the Nova Scotia Community College website that we can use?

**Me (1:09:10 PM):** cybersecurity@nscc.ca would be a better email address to use

**Mandy (1:10:04 PM):** Can the address be located on the Nova Scotia Community College website?

**Me (1:11:55 PM):** well... any @nscc.ca email is associated with our website and institution

**Mandy (1:12:39 PM):** I was unable to locate the email address on the website do you have a link where I can find the address please

**Mandy (1:12:42 PM):** in alternative we can complete the verification via postal letter We send a letter to the verified address listed on the order with a security code. When the letter arrives, a contact can then reach out to us, provide the code and complete the verification call.

OR

Legal opinion letter - In order to complete the validation process, the attached form must be completed, signed, and returned to DigiCert. To complete the form, you will need to consult with a licensed lawyer, accountant, or equivalent in your local jurisdiction. The form will be filled out by that representative and requires a valid signature. Once received, we will verify the legal standing of the signer through the proper registering authority and contact them, using publicly verified information, to verify the signature. Once the letter is signed, please attach it as a reply to this email or fax it to +1-801-705-0481. If the letter is signed by in-house counsel, please ensure that the registration records for the signer are up to date including contact information.

**Me (1:13:47 PM):** ok.. how about andre.klefenz@nscc.ca.... that should be findable on our employee directory and he's our IT infrastructure manager

**Me (1:14:34 PM):** https://www.nscc.ca/contact/employee-directory.aspx

**Mandy (1:16:58 PM):** Thank you for the link I have verified the email address Andre.Klefenz@nscc.ca and will send the verification email right away, just a moment please

**Me (1:17:34 PM):** thanks.. standing by

**Mandy (1:18:41 PM):** I have now sent the email to Andre.Klefenz@nscc.ca

**Mandy (1:20:43 PM):** Is there anything else I can assist you with?

**Me (1:22:04 PM):** I'm not sure.. who is going to get the token to create the txt record? me or Andre Klefenz?

**Me (1:22:14 PM):** Are there any other steps?

**Mandy (1:22:56 PM):** The domain nscc.ca has already been validated only the verification call is pending

**Mandy (1:23:15 PM):** nscc.ca

Successfully passed DCV check on 07 Mar 2025 15:01 UTC  
Valid for EV until 08 Apr 2026 15:01 UTC (12 months 3 days left)  
Valid for OV until 08 Apr 2026 15:01 UTC (12 months 3 days left)

DCV Method: email  
Date Submitted: 05 Mar 2025 14:05 UTC  
Email Used: webmaster@nscc.ca

**Me (1:23:39 PM):** great.. so we

**Me (1:23:45 PM):** 'we're good to go?

**Mandy (1:24:15 PM):** Yes once the verification email to Andre.Klefenz@nscc.ca has been approved we will complete the review and the certificate will be issued

**Me (1:24:30 PM):** perfect. thanks again

**Mandy (1:24:48 PM):** You are most welcome, is there anything else I can assist you with?

**Me (1:25:06 PM):** no. I think that is all.

**Mandy (1:25:24 PM):** Thank you for visiting have a great day further

## Technical Details

**Certificate Information:**
- **Domain:** support.nscc.ca
- **Primary Domain:** nscc.ca
- **DCV Status:** Passed (March 7, 2025)
- **Validation Type:** Email (webmaster@nscc.ca)
- **EV Valid Until:** April 8, 2026
- **OV Valid Until:** April 8, 2026

**Final Verification Contact:**
- **Name:** Andre Klefenz
- **Email:** andre.klefenz@nscc.ca
- **Role:** IT Infrastructure Manager
- **Verification Method:** Public employee directory
- **Directory URL:** https://www.nscc.ca/contact/employee-directory.aspx
