# RE-WebApps

This ReadMe file will always have the most recent status update of this project. The purpose of this project is to create a web application that allows for real-time messaging, as well as potential file sharing and extra security features along with this. There will also be real-estate data (looking into a Zillow API) and a ticketing system that assigns different leads to different sales reps (much like a CRM).

UPDATES/NEW FEATURES:
- Front-end created (will update css)
- Leads render to home page
- User login/registration created
- User groups created: Admin, Manager, Sales Team
-- Admin: all permissions, Manager: Viewing permissions on admin site, Sales Team: no admin-site permissions
- "Create Lead" page created and functional

CURRENT STATUS: Still working on the "CRM" aspect of the website, users can create their own leads but the following still needs to be done for this part of the website to be fully functional:
  - Create drop-down showing and saving the lead status
  - Designate leads to certain users
  - Block signed in users from seeing other user's leads (with the exception of managers who can see it in the Django Admin site)
  - Create drop-down showing lead status and create lead organization by status
  - Gather data on sold leads to show how many properties each user has sold within the past month/quarter
