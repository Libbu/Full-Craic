# Thriving Together

Thriving Together is a learner wellness community initiative aiming to showcase wellness resources, sessions, and healthy food options available to students in the learner environment.

The intended consumers of the information in this resource are students, whilst site adminstrators which include instructors, therapists and those responsible for food provision are able to showcase their offerings, planned sessions, or share their wisdom in a blog format.

The website features three sections: The home page takes users to posts on the subjects of wellness, the primary driver behind the initiative. A seperate food section features information available concerning healthy food in the immediate vicinity. A profiles session lists information about site contributors so that users can get to know those responsible for the site content and their background. 

![Landing Page](https://github.com/Libbu/Full-Craic/blob/main/media/deployedwithcards.JPG)


## UX

The visual theme of the website was inspired by popular wellness brand colour palattes as identified by [Hello CoCreator](https://hellococreator.com/2023/09/14/best-color-palettes-wellness/)

We encorporated various assets and content relevant to the themes of wellness in order to enhance the user experience; Some examples of these are soothing images promoting the wellness aestehtic on posts, and a coherent colour scheme throughout the website.

The sites navigation has been kept very simple to adhere to the Minimum Viable Product (MVP) concept. On arrival at the website users are invited to explore different sections, register or sign in. Once they are signed in the navigation changes slightly so that the option to logout presents instead. Logged-in users are able to leave comments. Site administrators are able to create content and approve comments from users from the Django adminstrative-panel.

## User Stories


- As a **student** I can **browse wellbeing content** so that I can be **informed about what is available to me**.
- As a **student** I can **register an account** so that I can **comment on posts**.
- As a **therapist/instructor** I can **include a section about me** so that users can **learn more about who is writing the content**.
- As a **food vendor** I can **include posts about healthy eating options** so that **students are aware of their choices**. 
- As a **student** I **can leave comments** on the site to **engage with site-owners/confirm attendence**.
- As a **therapist/instructor** I can **create posts** to the relevant section of the page **to share information with users**.
- As a **site owner** I **want visitors to the page to see a list of linked social media accounts** so that they can **follow me on other platforms**.
- As a **student** I am able to **indicate what wellness content interests me** so that I can **receive information relevant to my interests**.
- As a **student** I will **see community feedback** so that I can **see the quality of the resources provided**.
- As a **student** I am able to **view a record of sessions** I've attended so that **I know what I've done**.


## Scope

### High-Level Features

| **Wellness Blog Landing Page**   | **Food Offerings Landing Page**   | **Posts Details Page** | **Website as a whole** |
|---|---|---|---|
| List of posts  | List of posts | Post Content | Site nav bar |
| Posts load on click | Posts load on click | Comment Section| Footer with social media links |
| | | | Sign-in/up/out options |
| | | |Aesthetic wellness images |


|  **Feature** | **Value**  |  **Effort** |
|---|---|---|
| Landing Page  |  High |  Medium |
| Paginated List of Posts  | High  |  Medium |
| User Registration  | High  | High  |
| Navbar  |  High | Low  |
| Footer    | Medium  |Low   |
| Users Can Comment | High | High |
| Admin Can Publish Posts |  High | High |
| Wellness Aesthetic in Design    | High  |Low   |
| Ability to comment | High | High |
| Users Can Leave Reviews|  High | Medium |

| Feature  |  Priority |
|---|---|
| Landing Page | 1  |
| Paginated Posts | 1 |
| Food Section | 2  |
| Contributor Profiles Section | 2  |
| Sign-in  | 1 |
| New User Registration | 1  |
| Logout | 1  |
| Ability to Comment | 1  |
| Details of Sessions display when posts are clicked on | 1 |
| Wellness Design Aesthetic | 3  |
| Navigation Menu | 1 |
| Footer | 1  |

- __Navigation Bar__

  - Featured on all sections of the webiste, the fully responsive navigation bar includes links to the main landing page (home), the food section, and a meet the team section for contributor profiles. It is identical in each page to allow for easy navigation.

  - The navigation bar allows the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.

  - Options visibile on the navigation bar will change depending on whether the user is signed in or not. 

![Nav Bar](https://github.com/Libbu/Full-Craic/blob/main/media/navbar.JPG)

- __The homepage background image__

  - The landing page background image is a high quality photograph depicting a peacefull and relaxing scene.
  - Providing a backdrop for our posts, it visually reinforces the page aesthetic.

![Landing Page](https://github.com/Libbu/Full-Craic/blob/main/media/soothingimage.jpg)

- __Paginated Posts for Sessions/Blogs/Other Wellness Content__

  - This section invites the user to delve more deeply into our content by clicking on the post card to read what our contributors have had to offer.

![Landing Page](https://github.com/Libbu/Full-Craic/blob/main/media/deployedwithcards.JPG)

- __The Footer__ 

  - The footer includes links the user can follow to access our social media content on different platforms, encouraging them to stay connected with our wellness resources.

  - The footer displays consistently across all pages and is responsive on mobile. 

![Footer](https://github.com/Libbu/Full-Craic/blob/main/media/footer.JPG)

- __Registration, Sign In, and Sign Out pages__

  - These forms allow users to register for our website, registration is neccessary so that they can comment on contributor posts where this facility is allowed. 

  - These sections are valuable, therefore registration is possible with minimal fuss, and forms are styled to reflect our wellness aesthetic.

![Registration](https://github.com/Libbu/Full-Craic/blob/main/media/regform.JPG)
![Signin](https://github.com/Libbu/Full-Craic/blob/main/media/login.JPG)
![Signout](https://github.com/Libbu/Full-Craic/blob/main/media/signoutbutton.JPG)

- __The Detail of Session and Profile Posts__ 

  - These are where the substance of our wellness content lies. An eye-catching header image encourages the viewer to read further, revealing new information about sessions on offer to them as well as the time and location of these. On Food and Meet the Team sections of the website, it is expected that these posts will contain information about healthy food offerings on campus, and contrinutors to our page content. 

![Post Detail](https://github.com/Libbu/Full-Craic/blob/main/media/postdetail.JPG) 


- __The Comment Box__ 

  - Only visible to logged-in users, the comment box allows engagement on posts, whether this be to confirm attendance at a session, or feedback about a specific piece of content. Comments must be approved by site administrators.

![Comment Box](https://github.com/Libbu/Full-Craic/blob/main/media/commentbox.JPG) 

## Structure 

### Low Fidelity Wireframes

- __Desktop Landing Page__

![Low Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidlandpage.png) 

- __Desktop Post/Session Detail__

![Low Fi BlogPost](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidblogpost.png) 

- __Registration Form__

![Low Fi Registration](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidsignup.png) 

- __Home Page Mobile View__

![Low Fi LandingMob](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidlandmob.png) 

- __Post/Session Detail Mobile View__

![Low Fi Post detail Mob](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidsessionmob.png) 

- __Registration Form Mobile View__

![Low Fi Registration](https://github.com/Libbu/Full-Craic/blob/main/media/lowfidsignup.png) 

### High Fidelity Wireframes

- __Desktop Landing Page__

![High Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/hifidland.png) 

![High Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/himobilehomeheader.png) 

![High Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/himobilehome.png) 

- __Desktop Post/Session Detail__

![High Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/highfiddetailpost.png) 

![High Fi Landing](https://github.com/Libbu/Full-Craic/blob/main/media/hipostdetail.png) 


## Surface

### Design

#### Chosen Colours

A site palette was chosen from those highlighted on [Hello CoCreator](https://hellococreator.com/2023/09/14/best-color-palettes-wellness/)

The Palette chosen was:

![palette](https://github.com/Libbu/Full-Craic/blob/main/media/palattewellness2.jpg)

#### Media

Images are used to enhance UX and the aesthetic feel of our wellness site throughout.


## Database Design

The Entity Relationship Diagram reflecting our deployed project is as follows:

![ERD](https://github.com/Libbu/Full-Craic/blob/main/media/erd1.png)

Having developed in line with separation of concern principles, we feel in the future our database models and relationships can be simplified and utilised to meet the same stake-holder goals with additional views logic. An example of how relationships and models within this database could look is below, however we are still excited to see how our project could evolve in the hands of users.

![ERD2](https://github.com/Libbu/Full-Craic/blob/main/media/erd2.png)

## Technologies Used

- HTML
- CSS
- Bootstrap
- JavaScript
- Python
- Django 

## Testing

Testing of site functionality was done manually during development and post deployment.

It is our intention to carry out automated tests as part of routine app maintenance.

- CSS
No errors were found when passing through [CSS Validation](https://jigsaw.w3.org/css-validator/)

![CSS](https://github.com/Libbu/Full-Craic/blob/main/media/csstest.png)

- JavaScript

An Error was found when passing the JavaScript files through [JS Hint](https://jshint.com/) this pertained to a console log to check for connection which has been removed in deployment.

![JS](https://github.com/Libbu/Full-Craic/blob/main/media/jetest1.png)
![JS](https://github.com/Libbu/Full-Craic/blob/main/media/jetest2.png)


### Validating

## User Story Testing

1. As a **student** I can **browse wellbeing content** so that I can be **informed about what is available to me**.
- The wellbeing section of our site displays on arrival and posts can be accessed by clicking on the relevant cards.

![Landing Page](https://github.com/Libbu/Full-Craic/blob/main/media/deployedwithcards.JPG)



2. As a **student** I can **register an account** so that I can **comment on posts**.
- upon arriving at our website users are able to register accounts which grants them access to the facility to post comments in the wellbeing section.

![Registration](https://github.com/Libbu/Full-Craic/blob/main/media/regform.JPG)
![Signin](https://github.com/Libbu/Full-Craic/blob/main/media/login.JPG)

- We do not feel that comment functionality needs to exist for the meet the team section and so it is not implemented.


3. As a **therapist/instructor** I can **include a section about me** so that users can **learn more about who is writing the content**.
- Site admins are able to post, edit and remove a profile to the "Meet the Team" section of the website. They can add an image to their profile which will display.

![Landing Page](https://github.com/Libbu/Full-Craic/blob/main/media/meettheteam.JPG)


4. As a **food vendor** I can **include posts about healthy eating options** so that **students are aware of their choices**.
- functionality to enable display of posts in the Food section of the webpage is due to be deployed at a later date. As a stand-in measure food vendors are able to make use of the post functionality in the general wellness section to communicate about their offerings.


5. As a **student** I **can leave comments** on the site to **engage with site-owners/confirm attendence**.
- Students who have registered are able to leave comments under posts about wellbeing sessions. They can use these to confirm attendence, or simply to engage with the content.

![Comment Box](https://github.com/Libbu/Full-Craic/blob/main/media/commentbox.JPG) 

6. As a **therapist/instructor** I can **create posts** to the relevant section of the page **to share information with users**.
-Therapists, Instructors and other site admins can create posts that publish to the wellbeing section of the website.


7. As a **site owner** I **want visitors to the page to see a list of linked social media accounts** so that they can **follow me on other platforms**.
-A list of social media links display in the footer at the bottom of each page.

![Footer](https://github.com/Libbu/Full-Craic/blob/main/media/footer.JPG)

8. As a **student** I am able to **indicate what wellness content interests me** so that I can **receive information relevant to my interests**.
-Due to prioritisation this feature is not ready for deployment at the time of writing. As development work has been underway on it, we hope to include it in a later release.


9. As a **student** I will **see community feedback** so that I can **see the quality of the resources provided**.
- Other users comments underneath posts in the wellness section show to all site visitors. We plan to deploy this feature for our food section at a later date. 


10. As a **student** I am able to **view a record of sessions** I've attended so that **I know what I've done**.
- Due to prioritisation this feature has been moved to a future release.


### Features For Future Implementation

- User Types

Moving forward we would like to see front-end functionality that allows recognition of user types and a user-friendly front-end for site admins from which they can write and post their content. 

![fururelogin](https://github.com/Libbu/Full-Craic/blob/main/media/adminloginfrontend.png) 

The Food section of the website is still in development and requires database work to complete. Currently we have a placeholder image conveying to users that they can expect some delicious content in the future.

![foodcoming](https://github.com/Libbu/Full-Craic/blob/main/media/foodcomingsoon.JPG) 

## Known Issues and Bugs

On desktop our signout button is currenly stretching to the left. 

![stretchy](https://github.com/Libbu/Full-Craic/blob/main/media/stretchysignout.JPG) 

Currently the edit functionality does not work on comments. Posts made my site admins have full CRUD functionality.

## Deployment

The website has been deployed through Heroku.

The live website can be found here:

LINK

## Credits 

### Content

Bootstrap 4 was used to assist in the structure and layout of the page.

Content from Code Institute's LMS modules were used for standard code across all pages of the app. 

Back-end functionality is heavily inspired by CodeInstitute walkthrough project: I Think Therefore I Blog

[Font Awesome](https://fontawesome.com/) was used across all pages for social media link icons.

Fonts are from [Google Fonts](https://fonts.google.com/)

### Media

### Acknowledgements

Further assistance gratefully received from CI tutors Iris, Kevin and Martin, and the wider CI slack community.

Unless otherwise noted all code and content is the work of Team Full Craic as part of the Gwent group’s 3rd 3-day Hackathon for their Code Institute Bootcamp.

### Team Full Craic:

- Elizabeth Spivey: Team Lead, Agile Project Management, Django configuration, Front-End and Back-End Development
- James Price: Database development Lead, Front-End and Back-End Development, UX
- Tyrel Morant: Front-End Development, UX/UI Implementation Lead
- Esther Njoku: UX/UI Design and Wireframing Lead


