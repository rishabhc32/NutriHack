# NutriHack
We are making an app to show nutrient information of food. With advent of easy access to junk food we have spoiled our eating habits. Which leads to health diseases like diabetes and obesity.

Therefore to get easy access to nutrient information of food we are making our app __NutriHack__. 

This is how it will work:
* User clicks the photo of the food.
* The picture is processed and send to servers.
* With some DL and server magic we identify the food.
* The food's nutrient information is sent back to user.

![Architecture Image 1](images/arch1.jpg)

## How it Works
* We capture the camera feed from device using `WebRTC`.
* When user cliks capture button, the captured image frame is sent to `flask` server through `URL multipart form data` in `POST` request.
* DL and Server magic:
  * Images are classified using CNN.
  * After classification food's nutrient information is extracted using `edamam API`.
  * The response `JSON` is sent back to the user.
* After receiving the response, nutrient info is displayed on user screen.

## Architecture Diagram
![Architecture Diagram 2](images/arch2.jpg)
