# Cookbook - online recipes for delicious sweets!

The website is desgined to gather all people that loves baking delicious sweets. The focus of the website is to allow users to upload own recipes to share with others in this community. 

![Mockup](documentation/mockup.png)


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

+ Admin:
    + As a Admin, I can edit and delete all the recipes to maintain content of the page.

## Desgin

![Color Pallette](documentation/palette.png)

I choose main color of brown darken-2 (#5d4037) from materialize color palette and added lighter or darker tones to make sure that works well togheter on to the website. 

## Wireframes

I created wireframes in the Balsamiq program as first visual concept of the website.

Mobile wireframe - [PDF file here](documentation/mobile_wireframe.pdf)

![Mobile wireframe](documentation/mobile_wireframe.png)

Desktop wireframe - [PDF file here](documentation/desktop_wireframe.pdf)

![Desktop wireframe](documentation/desktop_wireframe.png)

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

![Users collection](documentation/users-coll.png)


### Recipes Collection
![Recipe collection](documentation/recipe-coll.png)

# Technologies Used

## Languages Used
+ HTML5
+ CSS3
+ JavaScript
+ Python

## Libraries and Programs Used
+ [Git](https://git-scm.com/) - Git was used for version control.
+ [GitHub](https://github.com/) - GitHub was used for storing code and deploying the site.
+ [Gitpod](https://www.gitpod.io/) - GitPod was used for  building and editing my code.
+ [Heroku](https://www.heroku.com/) - Heroku was used to deploy the project.
+ [Flask framework](https://flask.palletsprojects.com/en/2.1.x/) - Flask was used to back end application and interaction with front end.
+ [Jinja2 templating](https://jinja.palletsprojects.com/en/2.11.x/templates/) - Jinja2 was used to iterate through data from backend for correct rendering on the front end.
+ [MaterializeCSS](https://materializecss.com/) - MaterializeCSS was used to desgin responsive website.
+ [jQuery](https://jquery.com/) - jQuery was used to implement JavaScript from Materialize library.
+ [MongoDB](https://www.mongodb.com/) - MongoDB was used to store recipes and users collections in the database.
+ [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - Chrome Developer Tools was used to help fix problem areas and identify bugs.
+ [Font Awesome](https://fontawesome.com/) - The icons for cookie logo, social media and buttons were taken from Font Awesome.
+ [Google Fonts](https://fonts.google.com/) - The font 'Lobster' cursive was imported from Google Fonts.
+ [CSS root variables](https://css-tricks.com/breaking-css-custom-properties-out-of-root-might-be-a-good-idea/) - CSS root variables was used to store global styling in it.
+ [Balsamiq](https://balsamiq.com/) - Balsamiq was used to make Desktop and Mobile Wireframes.
+ [Am I Responsive?](http://ami.responsivedesign.is/#) - Website used to create mockup image for this README file.
+ [Tinypng](https://tinypng.com/) - Tinypng was used to compress images.
+ [IMGbb](https://imgbb.com/) - IMGbb was used to upload the hero image with chocolate muffins.

# Testing
* The testing section is in a separate file, [here](TESTING.md).

# Deployment

## Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:
1. Prepare files needed:
    - Create requirements.txt with command
    ```bash
    pip3 freeze --local > requirements.txt
    ```
    - Create Procfile
    ```bash
    echo web: python app.py > Procfile
    ```

2. MongoDB
    - Create account on the mongoDB.
    - Create a shared claster (free).
    - Choose a name and closest region.
    - Add user and give him privilages to read and write any database.
    - Add IP address
    - In the Cluster tab create database of "Cookbook" and add two collections of "users" and "recipes"
    - In the "Overview" tab select "Connect" button. Select "Connect your application". Make sure to select correct driver and version - "Python" and "3.6 or later". Copy connection string which is your MONGO_URI with correct user name, password and database name.

3. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the region.

4. Connect with GitHub account:
    - Select "Deploy" option in Heroku tab.
    - Deployment method: Connect to GitHub
    - Search for repository name and Connect

5. Prepare the environment:
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the MONGO_URI value and your chosen SECRET_KEY value to the env.py file.
    - In the Settings tab, click on Reveal Config Vars.
    - Add the IP, PORT, SECRET_KEY and MONGO_URI values to the Config Vars in Heroku.

6. Automatic deploys:
    - Select "Enable Automatic Deploys"

7. Manual deploy:
    - Choose main/master brunch and select "Deploy Branch"

## Forking
1. Sign in to Github and go to my [repository](https://github.com/KlaudiaMatysiak/Cookbook)
2. Select the Fork button at the top right of the page.
3. The fork is now in your repositories.

## Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/KlaudiaMatysiak/Cookbook.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/KlaudiaMatysiak/Cookbook)

# Credits

## Images and recipes
| Link to the image | Image | Where is it used on the project? |
|:---:|:---:|:---:|
|[Click here](https://beszamel.se.pl/przepisy/ciastka-i-ciasteczka/przepis-na-babeczki-czekoladowe-z-borowkami-re-3Qt5-gja7-Yhzw.html) | Chocolate muffins with blueberries | Home Page
|[Click here](https://unsplash.com/photos/vdx5hPQhXFk) | White chocolate cake | Home Page
|[Click here](https://realfood.tesco.com/recipes/chocolate-muffins.html) | Chocolate muffins on the baking tray | Recipes Page
|[Click here](https://www.goodto.com/recipes/chocolate-cookies) | Stack of chocolate cookies | Recipes Page
|[Click here](https://www.loveandlemons.com/brownies-recipe/) | Chocolate brownie | Recipes Page
|[Click here](https://realfood.tesco.com/recipes/bakewell-tart.html) | Bakewell tart | Recipes Page
|[Click here](https://www.goodto.com/recipes/easy-raspberry-muffins) | Raspberry muffins | Recipes Page
|[Click here](https://www.recipetineats.com/lemon-tart/) | Lemon Tart | Recipes Page

## Code
+ Code was inspired by the Task Manager mini project tutorials by Tim Nelson.
+ [Login required decorator](https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator) - Login required decorator was used to make sure that user won't see conent that shouldn't have access to it, like edit or delete recipe.