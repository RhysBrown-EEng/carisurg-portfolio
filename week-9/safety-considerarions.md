# Safety Considerations

## HCI Safety Considerations

| Concern | Context | Mitigation | Residual Risk |
|------------|-------------|-------------|-------------|
| Alert Fatigue | Nurse receiving large amounts of audible alarms for critical patients may consequently ignore the alarms consciously or subconsciously | Only urgent patients get audible alarms while non urgent cases simply populate queue. | A large amount of false positive patient alarms may still induce alert fatigue|
| Patient may misunderstand the prompts | As patients are self-registering, a misunderstanding may induce incorrect triage. | Kiosk audibly explains symptoms of each condition with companion visuals. Patients also have the option to call a nurse. | Patients still need to know that they do not understand, some may fail to recognize this. |
| Patients may be illiterate and unable to self register. | Many people in the Caribbean are illiterate and will be unable to read the kiosk instructions. | System must make use of both auditory and visual aids to communicate points. | Aids can only help so much; a nurse may still be needed. |
## HRI Safety Considerations

| Concern | Context | Mitigation | Residual Risk |
|------------|-------------|-------------|-------------|
| Robot sensors may fail | ED-traversing robot may experience sensor failure. | Robot has 2 sensors for redundancy and shuts itself off when they disagree. | A dual sensor failure due to catastrophic damage may result in a failure to self-shutdown. |
| Robot may accidentally hurt patient | ED-traversing robot may accidentally drive into a patient or hit them with its arms. | Robot must be very conservative and slow in movements to prevent a mishap. | Fast-moving individuals may walk in the robots path before it can stop the impact. |
| Robot may fail to detect a high acuity level | ED-traversing robot may inspect a patient a erroneously deem them a lower acuity level and fail to inform nurses. | Careful sensor fusion and computer vision must be used to ensure a high recall, even if it means the robot must investigate a few false positives. | Not all patients will be caught regardless of the algorithm employed within in the robot. |

## Failure Modes

| Failure Event | Setting A - HCI |  Setting B - HRI  | 
|------------|-------------|-------------|
| Lost Connectivity | Wired back up connection transfers data to nurse's tablet devices; mobility of nurses limited | Robot must physically inform nurses of deteriorating patients. |
| Lost Power | Kiosk has battery backup to remain functional without external power. | Battery is used to provide 6 hours of standby power.|
| Incorrect data entry | Kiosk seeks confirmation but ultimately cannot triage accurately if patient information is false. | Battery is used to provide 6 hours of standby power. |