from flask import flash, jsonify, redirect, render_template, request, url_for, escape
from app import app, db
from database_setup import init_db
from models import MenuItem, Restaurant

init_db()


#JSON APIs to view Restaurant Information
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurantToShow = Restaurant.query.get_or_404(restaurant_id)
    menuItems = MenuItem.query.filter_by(restaurant_id=restaurant_id).all()

    return jsonify(menuItems=[menuItem.serialize for menuItem in menuItems])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = MenuItem.query.filter_by(id=menuItem_id).first()

    return jsonify(menuItem=menuItem.serialize)

@app.route('/menu/<int:menuItem_id>/JSON')
def showMenuItemJSON2(menuItem_id):
    menuItem = MenuItem.query.filter_by(id=menuItem_id).first()

    return jsonify(menuItem=menuItem.serialize)

@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = Restaurant.query.order_by(Restaurant.id).all()
    return jsonify(restaurants= [r.serialize for r in restaurants])


#Show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    restaurants = Restaurant.query.order_by(Restaurant.name).all()
    return render_template('restaurants.html', restaurants = restaurants)

#Create a new restaurant
@app.route('/restaurant/new/', methods=['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])

        db.session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        db.session.commit()

        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')

#Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods = ['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = Restaurant.query.get_or_404(restaurant_id)

    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
          
            flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
            return redirect(url_for('showRestaurants'))
    else:
         return render_template('editRestaurant.html', restaurant = editedRestaurant)


#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods = ['GET','POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = Restaurant.query.get_or_404(restaurant_id)

    if request.method == 'POST':
        db.session.delete(restaurantToDelete)
        flash('%s Successfully Deleted' % restaurantToDelete.name)
        db.session.commit()

        return redirect(url_for('showRestaurants', restaurant_id = restaurant_id))
    else:
        return render_template('deleteRestaurant.html', restaurant = restaurantToDelete)

#Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    items = MenuItem.query.filter_by(restaurant_id = restaurant_id).all()

    return render_template('menu.html', items = items, restaurant = restaurant)
     

#Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new/',methods=['GET','POST'])
def newMenuItem(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], course = request.form['course'], restaurant_id = restaurant_id)
        db.session.add(newItem)
        db.session.commit()

        flash('New Menu %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)

#Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = MenuItem.query.get_or_404(menu_id)

    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']

        db.session.add(editedItem)
        db.session.commit() 

        flash('Menu Item Successfully Edited')
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)


#Delete a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    menuItemToDelete = MenuItem.query.get_or_404(menu_id)

    if request.method == 'POST':
        db.session.delete(menuItemToDelete)
        db.session.commit()

        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item = menuItemToDelete)




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
