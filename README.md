# Health Lab API
The Health Lab API is a software interface that allows developers to integrate health-related data into their applications, enabling access to resources such as patient data and medical records through standardized programming commands. 

The API is built with Django Rest Framework and Spectacular for making OpenAPI docs. It's secured with JWT Authentication (SimpleJWT).

## Version: 1.0.0

### /api/login/

#### POST
##### Description:
Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful login |

### /api/orders/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of orders |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/orders/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Order ID to retrieve details | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of order details |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/orders/{id}/delete/

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Order ID to delete | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No content (Successful deletion) |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/orders/{id}/update/

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Order ID to update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful update of order |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Order ID to partially update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful partial update of order |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/patient_profile/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Patient ID to retrieve profile | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of patient profile |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/patients/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of patients |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/patients/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Patient ID to retrieve details | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of patient details |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/patients/{id}/delete/

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Patient ID to delete | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No content (Successful deletion) |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/patients/{id}/update/

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Patient ID to update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful update of patient details |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Patient ID to partially update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful partial update of patient details |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/refresh/

#### POST
##### Description:
Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful token refresh |

### /api/results/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of results |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/results/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Result ID to retrieve details | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful retrieval of result details |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/results/{id}/delete/

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Result ID to delete | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No content (Successful deletion) |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

### /api/results/{id}/update/

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Result ID to update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful update of result |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | Result

 ID to partially update | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful partial update of result |

##### Security

| Security Schema | Scopes |
| --- | --- |
| jwtAuth | |
