
# Flask-REST-API

This is a Flask application that serves as a RESTful API for managing items, stores, tags, and user authentication. The API provides functionality for tasks such as retrieving, creating, updating, and deleting items and stores. It enables the association of tags with stores, linking items to tags, and supports user registration, login, and logout processes. Implemented with Flask-Smorest for API documentation and validation, Flask-JWT-Extended for user authentication using JSON Web Tokens (JWT), and SQLAlchemy for database interactions, the application is organized using Flask Blueprints for modularity and scalability. This backend system is designed for use in scenarios such as inventory management or e-commerce platforms.

### `GET /items/<int:item_id>`
- **Description:** Retrieves details of a specific item by its ID.
- **Method:** GET
- **Parameters:**
  - `item_id` (int): The ID of the item to retrieve.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Item details in the format specified by the `ItemSchema`.

### `DELETE /items/<int:item_id>`
- **Description:** Deletes a specific item by its ID. Requires admin privileges.
- **Method:** DELETE
- **Parameters:**
  - `item_id` (int): The ID of the item to delete.
- **Authorization:**
  - Requires a valid JWT token with admin privileges.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Message indicating successful deletion.

### `PUT /items/<int:item_id>`
- **Description:** Updates or creates an item by its ID.
- **Method:** PUT
- **Parameters:**
  - `item_id` (int): The ID of the item to update or create.
- **Authorization:**
  - Requires a valid JWT token.
- **Request Payload:**
  - Body: Data for updating the item in the format specified by `ItemUpdateSchema`.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Updated item details in the format specified by `ItemSchema`.

### `GET /item`
- **Description:** Retrieves a list of all items.
- **Method:** GET
- **Response:**
  - Status Code: 200 (OK)
  - Body: List of items in the format specified by `ItemSchema` (many=True).

### `POST /item`
- **Description:** Creates a new item.
- **Method:** POST
- **Authorization:**
  - Requires a valid JWT token.
- **Request Payload:**
  - Body: Data for creating the new item in the format specified by `ItemSchema`.
- **Response:**
  - Status Code: 201 (Created)
  - Body: Details of the newly created item in the format specified by `ItemSchema`.



#### `GET /store/<int:store_id>`
- **Description:** Retrieves details of a specific store by its ID.
- **Method:** GET
- **Parameters:**
  - `store_id` (int): The ID of the store to retrieve.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Store details in the format specified by the `StoreSchema`.

#### `DELETE /store/<int:store_id>`
- **Description:** Deletes a specific store by its ID.
- **Method:** DELETE
- **Parameters:**
  - `store_id` (int): The ID of the store to delete.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Message indicating successful deletion.

#### `GET /store`
- **Description:** Retrieves a list of all stores.
- **Method:** GET
- **Response:**
  - Status Code: 200 (OK)
  - Body: List of stores in the format specified by `StoreSchema` (many=True).

#### `POST /store`
- **Description:** Creates a new store.
- **Method:** POST
- **Request Payload:**
  - Body: Data for creating the new store in the format specified by `StoreSchema`.
- **Response:**
  - Status Code: 201 (Created)
  - Body: Details of the newly created store in the format specified by `StoreSchema`.


#### `GET /store/<int:store_id>/tag`
- **Description:** Retrieves a list of tags associated with a specific store.
- **Method:** GET
- **Parameters:**
  - `store_id` (int): The ID of the store to retrieve tags from.
- **Response:**
  - Status Code: 200 (OK)
  - Body: List of tags in the format specified by `TagSchema` (many=True).

#### `POST /store/<int:store_id>/tag`
- **Description:** Creates a new tag for a specific store.
- **Method:** POST
- **Parameters:**
  - `store_id` (int): The ID of the store to associate the new tag with.
- **Request Payload:**
  - Body: Data for creating the new tag in the format specified by `TagSchema`.
- **Response:**
  - Status Code: 201 (Created)
  - Body: Details of the newly created tag in the format specified by `TagSchema`.

#### `POST /item/<int:item_id>/tag/<int:tag_id>`
- **Description:** Links a tag to an item.
- **Method:** POST
- **Parameters:**
  - `item_id` (int): The ID of the item to link the tag to.
  - `tag_id` (int): The ID of the tag to link to the item.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Details of the linked tag in the format specified by `TagSchema`.

#### `DELETE /item/<int:item_id>/tag/<int:tag_id>`
- **Description:** Unlinks a tag from an item.
- **Method:** DELETE
- **Parameters:**
  - `item_id` (int): The ID of the item to unlink the tag from.
  - `tag_id` (int): The ID of the tag to unlink from the item.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Message indicating successful unlinking, along with item and tag details.

#### `GET /tag/<int:tag_id>`
- **Description:** Retrieves details of a specific tag by its ID.
- **Method:** GET
- **Parameters:**
  - `tag_id` (int): The ID of the tag to retrieve.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Tag details in the format specified by the `TagSchema`.

#### `DELETE /tag/<int:tag_id>`
- **Description:** Deletes a specific tag by its ID if no items are tagged with it.
- **Method:** DELETE
- **Parameters:**
  - `tag_id` (int): The ID of the tag to delete.
- **Response:**
  - Status Code: 202 (Accepted)
  - Body: Message indicating successful deletion if no items are tagged with the specified tag.


#### `POST /register`
- **Description:** Registers a new user.
- **Method:** POST
- **Request Payload:**
  - Body: Data for registering a new user in the format specified by `UserSchema`.
- **Response:**
  - Status Code: 201 (Created)
  - Body: Message indicating successful user creation.

#### `POST /login`
- **Description:** Logs in a user and provides access and refresh tokens.
- **Method:** POST
- **Request Payload:**
  - Body: Data for logging in a user in the format specified by `UserSchema`.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Access and refresh tokens.

#### `POST /logout`
- **Description:** Logs out a user by adding their JWT token to a blocklist.
- **Method:** POST
- **Authorization:**
  - Requires a valid JWT token.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Message indicating successful logout.

#### `POST /refresh`
- **Description:** Obtains a new access token using a refresh token.
- **Method:** POST
- **Response:**
  - Status Code: 200 (OK)
  - Body: New access token.

#### `GET /user/<int:user_id>`
- **Description:** Retrieves details of a specific user by their ID.
- **Method:** GET
- **Parameters:**
  - `user_id` (int): The ID of the user to retrieve.
- **Authorization:**
  - Requires a valid JWT token.
- **Response:**
  - Status Code: 200 (OK)
  - Body: User details in the format specified by `UserSchema`.

#### `DELETE /user/<int:user_id>`
- **Description:** Deletes a specific user by their ID.
- **Method:** DELETE
- **Parameters:**
  - `user_id` (int): The ID of the user to delete.
- **Authorization:**
  - Requires a valid JWT token.
- **Response:**
  - Status Code: 200 (OK)
  - Body: Message indicating successful user deletion.

