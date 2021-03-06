# Cookbook - Testing

# User story

## First Time Visitor:
+ *As a First Time Visitor, I can immediately understand the purpose of the webiste.*
    + The first user landing on the website is Home page. User is welcomed with chocolate muffins with blueberries and brief message explaining the site's purpose.

        ![Home Page](documentation/feature-home-page.png)

+ *As a First Time Visitor, I can easily navigate the website to find content.*
    + I can easly navigate through the site and find desirable content.

        ![Navbar](documentation/feature-navbar-desktop.png)

+ *As a First Time Visitor, I can view recipes and choose one to read.*
    + I can select *Recipes* from navbar to view all the recipes.

        ![Recipes](documentation/feature-recipes.png)

    + I can select the recipe that draws my attention. It redirects me to the selected recipe, where I can read list of ingredients and method of preparation. 
    + During testing I decided to add "GO BACK" button for more user friendly experience. 

        ![Selected recipe](documentation/full-recipe.png)

+ *As a First Time Visitor, I can search for the desire recipe.*
    + I can search for recipe by title or ingriedients list item. I searched "almonds" and I got result of "Bakewell Tart". Future Improvement: displaying what user was looking for.

        ![Found Recipe](documentation/almonds.png)

    + When there is no results found there is message displayed "No Results Found"

        ![No results](documentation/no-results.png)

+ *As a First Time Visitor, I can register an account.*
    + I can register account just by adding username and password. 

        ![Register account](documentation/feature-register-desktop.png)

    + After registration is complete I'm redirected to the Recipes Page with message "Registration Successfull"

        ![Registration Successfull](documentation/registration-successfull.png)
    
    + I need to pass requirements to successfully register account.

        ![Registration requirements](documentation/registration.png)

    + I can't register account with the name already taken.

        ![User already exists](documentation/user-exists.png)


+ Returning Visitor:
+ *As a Returning Visitor, I can log in.*
    + I can log in by username and password that I provided during registration process.
    + After successfull login, it redirected me on the recipes page with Welcome message.

        ![Welcome message](documentation/login-message-desktop.png)

+ *As a Returning Visitor, I can log out.*
    + On the large devices I can log out by clicking my username on the navbar and select "Log Out"

        ![User dropdown menu](documentation/feature-user-dropdown-desktop.png)
    + On the mobile devises I can log out by clicking on the hamburger button and select "Log Out"

        ![Mobile dropdown menu](documentation/mobile-dropdown-menu.jpg)
    
    + If I fill login form with incorrect values I'm redirected to login page again with message "Incorrect Username and/or Password"

        ![Login failed](documentation/login-incorrect.png)

+ *As a Returning Visitor, I can create recipe so other can view it.*
    + I can add recipe while I'm log in by choosing "Add recipe" link from navigation bar and it redirect me on the page with form that I can add recipe. I need to provide title for the recipe, ingredients 1 per line, preparation method with one step per line and recipe image with URL.

        ![Add recipe page](documentation/feature-add-recipe-desktop.png)
    
    + After adding the recipe it redirected me on the recipes page with message displayed "Recipe successfully added" and testing recipe added as a last recipe on the page.

        ![Added recipe message](documentation/message-recipe-added.png)

        ![Test recipe](documentation/test-recipe.png)

+ *As a Returning Visitor, I can edit recipe to change any mistakes.*
    + I can edit my own recipes by clicking on the green button "EDIT" on the recipes page. 

        ![Edit button](documentation/edit-button.png)

    + It redirected me on the page with form to edit selected recipe. 

        ![Test edit recipe](documentation/test-edit-recipe.png)

    + I can cancel the process by selecting the red button "CANCEL" and it redirects to the recipes page or I can save editng process by selecting the brown button "EDIT RECIPE" and it redirect me to the selected recipe page with message "Recipe successfully updated"

        ![Recipe edited](documentation/test-edited-recipe.png)

+ *As a Returning Visitor, I can delete recipe.*
    + I can delete my own recipes by selecting the red button "DELETE" on the recipes page.

        ![Delete button](documentation/delete-button.png)
    
    + After choosing "DELETE" button it showed up window asking me if I am sure of deleting the recipe and two optiion to choose: "NO" and "YES".

        ![Delete modal](documentation/test-delete-modal.png)
    
    + After choosing "NO" it redirects me to the recipes page.

    + After choosing "YES" it redirects me to the recipes page with message "Recipe Successfully Deleted!" and it deletes recipe from the page.

        ![Deleted recipe](documentation/recipe-deleted-message.png)

+ Admin:
+ *As a Admin, I can edit and delete all the recipes to maintain content of the page.*
    + As Admin I have access to edit and delete all the recipes on the page.

        ![Admin view](documentation/admin-view.png)

# Validators

## HTML Validator [W3C](https://validator.w3.org/nu/)

![HTML Validator](documentation/validator-html.png)

Direct links:
+ [Home](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/home)
+ [Recipes](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/get_recipes)
+ [Log In](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/login)
+ [Register](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/register)
+ [Selected Recipe](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/recipe/6258721129fb8507f067d2a6)
+ [Delete Recipe](https://validator.w3.org/nu/?doc=https://cookbook-km.herokuapp.com/delete_recipe/6258721129fb8507f067d2a6)

## CSS Validator [Jigsaw](https://jigsaw.w3.org/css-validator/)

![CSS Validator](documentation/validator-css.png)

## JavaScript [JSHint](https://jshint.com/)

![JavaScript Validator](documentation/validator-js.png)

## Python [pep8online](http://pep8online.com/)

![Python Validator](documentation/validator-pep8.png)

# Lighthouse DevTools

![Lighthouse](documentation/lighthouse.png)

![Lighthouse](documentation/lighthouse-recipes.png)

![Lighthouse](documentation/lighthouse-selectedrecipe.png)

![Lighthouse](documentation/lighthouse-addrecipe.png)

# Devices

## Google Chrome

![Google Chrome](documentation/chrome.png)

## Mozilla Firefox 

![Firefox](documentation/mozilla.png)

## Edge

![Edge](documentation/edge.png)

## iPhone 12 Pro

![iPhone 12 Pro](documentation/ihpone12pro.jpg)

# Bugs

## Fixed

1. CSS and JavaScript files not connected.

    Edit recipe templated wasn't connecting with CSS and JavaScript files. I fixed it by replacing relative path with jinja url_for function in the base.html file. 

    ```
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    ```

    ```
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    ```

    ![CSS and JavaScript](documentation/css-javascript.png)

2. Unnecessary whitespaces from Jinja rendered template

    While it was rendering data from mongodb there was plenty unnecessary whitespaces. I've tried to use minus symbol in the beginnig and in the end of jinja template but it wasn't working. Instead of using for loop I read array from database with join function.

    Instead:

    ```
    {%- for ingredient in ingredient -%}
        {{ ingredient }}
    {%- endfor -%} 
    ```
    I implemented code:
    ```
    <textarea id="ingredients" name="ingredients" class="materialize-textarea" required>{{ recipe.ingredients|join("\n") }}</textarea>
    ```

    ![Unnecessary whitespaces](documentation/edit-recipe-bug.png)

3. Visible delete recipe modal in source code

    Delete modal was visible in the source code for users that wasn't author of the recipe. It was causing the problem because everyone had access to modal where you can delete recipe. I fixed that with moving whole modal to the recipe loop.

    ![Delete modal bug](documentation/modal-bug.png)

4. Displaying two flash messages at once.

    After deleting the recipe user could see two flash messages. I fixed that by putting second flash message in the else statement.

    ![Two messages bug](documentation/bug-two-messages.png)

5. User access to the edit page with direct link not being log in.

    If user had access to the direct link for the edit recipe could see the content of the page. To fix that I applied @login_required decorator.

    ![User access](documentation/bug-user-access.png)

6. Cookie Font Icon had position bug on the mobile devices.

    On the mobile devices there was problem with line height so to fix that I applied css rule of line height for the cookie icon to make sure that is all straight.

    ```
    @media only screen and (max-width: 600px) {
        a.right.brand-logo.cookbook-logo > i {
            line-height: 56px;
        }
    }
    ```

    ![Icon bug](documentation/bug-icon.png)

    ![Mobile icon bug](documentation/mobile-bug-icon.png)

## Unfixed

1. Unknown bug with dropdown menu on the apple device

    I'm aware about bug that happens on the apple device iPhone 12 Pro. Mobile dropdown menu is not working precisly all the time. Sometimes when user choose to go on the Login page it loads Register. It looks like sometimes the position of the dropdown menu is not precise. This issue only occur on the apple devices because on the android works well.