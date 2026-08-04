# System Requirements

Name: Rhys Brown

## System Requirements
| Inputs  | Outputs | 
|-------|-----|
| 1. Data entered via wearable and manual data entry. <br> 2. Camera to detect user actions and presence to help the user.| 1. Acuity level (based on ESI scale) <br> 2. Directions for patient to where they must go based on acuity level in the ED.  | 

## System Requirements

| Functional  | Non-functional | Integration  |
|-------|-----|------------|
| 1. Display must show triage score within 5 seconds of processing. <br> 2. Audio alerts must be limited to critical (ESI 1-3) patients to reduce alert fatigue. <br> 3.Prominent "Call Staff" panic button must immediately notify ED personnel and pause self-registration. | 1. System must use no more than 5 major colors to increase uniformity and ensure alerts have contrast. <br> 2. Kiosk must self sanitize after every use. <br> 3. Kiosk must terminate session upon 60 seconds of inactivity and no user being physically present so patient data cannot be accessed by other patients.  | 1. System stores data on local kiosk machine and manually backs it up to server every minute. <br>  2. Acuity levels must sync with nurse tablets immediately.   |