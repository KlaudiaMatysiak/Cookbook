# Cookbook - online recipes for delicious sweets!

The website is desgined to gather all people that loves baking delicious sweets. The focus of the website is to allow users to upload own recipes to share with others in this community. 

![Mockup](/documentation/mockup.png)

[View the live project here](https://cookbook-km.herokuapp.com/home)

# User Experience (UX)

## User Stories

+ First Time Visitor:
    + As a First Time Visitor, I can immediately understand the purpose of the webiste.
    + As a First Time Visitor, I can easily navigate the website to find content. 
    + As a First Time Visitor, I can view recipes and choose one to read.
    + As a First Time Visitor, I can search for the desire recipe.
    + As a First Time Visitor, I can register an account.

+ Returning Visitor:
    + As a Returning Visitor, I can log in.
    + As a Returning Visitor, I can log out.
    + As a Returning Visitor, I can create recipe so other can view it.
    + As a Returning Visitor, I can edit recipe to change any mistakes.
    + As a Returning Visitor, I can delete recipe.

## Desgin

![Color Pallette](/documentation/palette.png)

I choose main color of brown darken-2 (#5d4037) from materialize color palette and added lighter or darker tones to make sure that works well togheter on to the website. 

## Wireframes

I created wireframes in the Balsamiq program as first visual concept of the website.

+ Mobile wireframe - [PDF file here](/documentation/mobile_wireframe.pdf)
![Mobile wireframe](/documentation/mobile_wireframe.png)

+ Desktop wireframe - [PDF file here](/documentation/desktop_wireframe.pdf)
![Desktop wireframe](/documentation/desktop_wireframe.png)

# Database

## Data Types
The types of data stored in MongoDB are:
* ObjectId
* String
* Array
* Binary

## Collection Structure
Cookbook relies on two database collections. 

### Users Collection
Password is entered as string, but stored as binary after encryption trough security werkzeug tool. To log in user - password from database is encrypted to check match with inserted data in the login form.

![Users collection](/documentation/users-coll.png)


### Recipes Collection
![Recipe collection](/documentation/recipe-coll.png)
