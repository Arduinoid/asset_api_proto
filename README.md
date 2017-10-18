# **_PROTOTYPE_** Asset Audit System API

This is a work in progress API that I am currently working on. Once I get the basic structure down I will push to a _non-prototype_ repo.

## Basic Usage

- Capture server hardware specifications in **JSON** format via **POST** request. This information will com from a minimal Linux based image that will **PXE** boot the server and send the audit info the the API.

- Other systems on the network will be able to consume the captured information using **GET** requests to the API. This will return **JSON** data

- Certain authenticated users will be able to replace attributes of a record using **PATCH** requests

- The Linux based image will be able to replace old records in the system using **PUT** requests if a chassis makes it back into inventory 

- The **DELETE** method will be available to authenticated users to remove inventory records.