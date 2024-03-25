<img src="" width="200" height="200" alt="TheBearaDirectory">



# Welcome to TheBearaDirectory

## A Blog Website.

> TheBearaDirectory is a blog about the Beara Peninsula situated in the SouthWest coast of Ieland

### [Link to the live site](https://the-beara-directory-blog-20bd8e403ed5.herokuapp.com/)

#### - By Gordon Meade

---

## Table of contents 

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---



## Database planning 

#### Data structure

<img src="static/images/Screenshot 2024-03-21 194328.png" alt="Lucid diagram" width="600">

- After deciding on the kind of the project and features I wanted to implement I used a lucidchart to plan the database structure.
- The above diagram is serving as an initial guide to indicate the types and relationships between data stored.

#### Data models

> User

-This is a Django predefined class incorporating an username & password to login



---


> Category model

| Name | Field |
| Name | CharField |

---

> Post model

| Name | Field |
| Title | CharField |
| Slug | SlugField |
| Body | TextField |
| Created on | DateTimeField |
| author | ForeignKey |
| Last Modified | DateTimeField |
| Catergories | ManyToManyField |


---


> Comment model

| Name | Field |
| author | CharField |
| Body | TextField |
| Created on | DateTimeField |
| post | ForeignKey |



---
## UX design


### Overview

#### Design

> Initial design planning

Early design stage of this project was created in Balsamic.


<img src="static/images/Screenshot 2024-03-21 200255.png" alt="Homepage design" width="520">
<img src="static/images/Screenshot 2024-03-21 200811.png" alt="Mobile Design" width="400">

I wanted the website to be easy to use by creating a simple design.

#### Site User

- Someone living in the Beara area.
- Tourists travelling to the area on holidays
- Someone who feels a connection to the Beara Peninsula and wants to fell a paret of the commuinity

#### Goals for the website

- To have an informative site on all the loactions and events in Beara
- To allow conversation through comments on specific topics 
- To allow users to creata and delete comments they create 





##### [ Back to Top ](#table-of-contents)

---

# Agile Development

## Overview

I used GitHub projects to develop my site. 
## User Stories

My User stories covered everything from installing Django to what i thought the user would like. I kept my functionality low in keeping with agile and concentrated on 
creating a MVP that can be added to over time

> List of User Stories

1. https://github.com/users/Gordon-Meade/projects/2/views/1
2. https://github.com/Gordon-Meade/thebearadirectory/issues/3
3. https://github.com/Gordon-Meade/thebearadirectoryblog/issues/4
4. https://github.com/Gordon-Meade/thebearadirectory/issues/2
5. https://github.com/Gordon-Meade/thebearadirectory/issues/1
6. https://github.com/Gordon-Meade/thebearadirectoryblog/issues/2
7. https://github.com/Gordon-Meade/thebearadirectoryblog/issues/3
8. https://github.com/Gordon-Meade/thebearadirectory/issues/5
9. https://github.com/Gordon-Meade/thebearadirectory/issues/4



##### [ Back to Top ](#table-of-contents)

---

# Features implemented




### Navbar and Footer:

- Navbar and footer are present on every page
- Navbar's content changes depending on user authentication, allowing access to Comments
- Footer includes Social Links

### Index page:

- The homepage provides the blogs created by the User
- It can be accessed without signing in.

### About Us page:

- Main page includes a short information about the blog


### Authentication and profile management:

- User can sign up to the site
- User can log in to their account
- User can delete their posts
- The authentication process is safe thanks to [Django-AllAuth](https://github.com/pennersr/django-allauth) and csrf tokens.

### Responsiveness:

- Website is responsive thanks to Bootstrap and media queries applied.
- There's a hamburger navbar on small devices.

##### [ Back to Top ](#table-of-contents)

---

# Features Left to Implement

- Expand the site to become more interactive for the user.
- Create a new app to include Events, Clubs
- Create a business section for companies to showcase their products

##### [ Back to Top ](#table-of-contents)

---

# Technology used 

- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for timeout in messages
- Django - framework used to build this project
- Bootstrap 5 - 
- Heroku PostgreSQL - used as the database
- Font Awesome - for social media icons
- Google Fonts- 
- GitHub - for storing the code and for the projects Kanban
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - version control tool

##### [ Back to Top ](#table-of-contents)

---

# Testing

### Responsiveness

I was testing for responsiveness in Google Chrome, using devtools


![Index page](/static/images/Screenshot-2024-03-25-071949.png)


> About Us page:

![about page](/static/images/Screenshot-2024-03-25-072135.png)


> Sign in page:

![welcome page](/static/images/Screenshot-2024-03-25-072317.png)


### Automatic Testeing

|Automatic tests| passed|



### Manual testing

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create profile | Pass |
| User can log into profile | Pass |
| User can log out of profile | Pass |
| Messages are displaying | Pass |
| Messages are dismissable by button and timeout | Pass |



---

#### User Navigation Tests

| Test | Result  |
|--|--|
| User can easily navigate through the site | Pass |
| User can access About  page| Pass|
| User access their account page|Pass|
| User can access the card content in blog|Pass|
| SuperUser can access admin page|Pass|



---

#### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page |Pass|
| Non authorised user can look at blog | Pass |
| Non authorised user cannnot comment on posts| Pass|



---

#### CRUD Tests

| Test |Result  |
|--|--|
|User can make a comment | Pass |
|User can edit a comment | Pass |
|User can delete a comment | Pass |
|User can read a comment | Pass |


#### Bugs and Issues

- Original design had an infinite error loop which was very hard to detect. This project had to be restarted due to this
- The new Repo had a similar issue so a new app was created and I reset the model to the walkthrough so that now its functional
- There was a bug in the code in relation to the edit/delete. an adjustment to the code fixed this
- I would have liked to have my Welcome page as my home page but Django wanted the blog page so i feel the UX could be better
- Time constrain due to start over hindered m abilit to deliver my original concept but I am happy I achieved a functional site


---

#### Thank yous & references
- Thank you David Calikes, Martin McInerny, Joe Melis and Tutor Support for your amazing help
- Django Documentation
- we3schools
- Code Institute - I think before I blog
- Bootstrap Documentation 