# Draw and Classify your handwritten digit!
A GUI with OpenCV and Tensorflow for drawing and classifying handwritten digit.

The GUI is made by OpenCV2. It allows you to draw digits freely(with "Mouse Event" trick!). <br>
A tensorflow model works as backend to classify each digit you drew.

All files come with detailed documents, so you can inspect the codes comfortably. <br>
Feel free to try it yourself! :)

## Demo:
Look at the app's performance:

<img src="https://lh3.googleusercontent.com/fife/AAbDypBX5mLCeqomrnMFoTbFknUTY3r_BlJ5phYIDXr4kLXvQbP4qr8RaPeNoOargDy0JExtC4cM2itF7iXDZusRuqlb83kmqd773mUoHBAM9dwOJ2gH17geCg_GF7ANxvPo86F7eyrdeBg5pp19-kd6l3eAe8D6tK37zX2AOJTzXCaeMNSnZDFm3bjZvz5ooK9hmMXrfD77WpNYbeXVazplbCDvuOczXI_97nex2oeLYw-4SBcOO5cW7E6aVe1IO7mKhvyqZrYqq5cUkQuS6etb5osj-wdhBB8sDnlePw_jEn86uoeOPmFAVNQikmduthASIwhRGA2oJJPZ9Y1eshxS6WnzinypbWX0JMmRrJzHAzN6r8ELP6nOGTPfXyGsuFWSBt2AD-zK65EsF0jQqIgB_GJT5lHuPaVD4oMXpFzV768h3eHuGJVRFT7Pll9BTQa4Njq4gbL_zRyCIZh5z9g_Lh46SPEQ7-H0F_N9hIMRm54pogCB6eBhCRBJiHEs69OKDYNdsHVO0_gQmjmJzZBB4nSJAzZEVsRVbJPZk80sHWMP6rncBsGW5CF6bJwlft2V_PvEdiNeP08vjNqlbARFK9obB1COP-gv145lvJC9Q_hXq1ZDwqmRAS-rM8oLMKS8YeKwvM2shJNaeY0bKhdOs_kike_uXnI-wFgWoVOtbRrTb6U4MIcvFRRDkgE2XpDXnFhejupteDIdUaYEpiSwDF2mfNMsV-SnXf86KstWZDWkk09_N2F4yacnGSVomh30zKzrVHRYI-kam4bPNWFyevoXTgeV3PVUM6YfIzcxBa5DpFUyCsq7sZDKo_4fwGb7rLeY5pnwhVkZJeKVmdnmSuRJnHtokMlRA0bpiHScYi4Or4_h9YsflFzrRzJIVINNHktsmO7nA-G_JD32noBo1m0gDgmgsD4KmLh5jAvDc7B_Q2PEsTT-lv9RkD2xM-1U5_9I-TZBjBfIkyO0dnG0rBWD0IF04SWsGndy0BRY-sSpll1a3__NOEcpqx9gra74XJXOyMRnJsc-xS50X7nidTL7CeRALb7SKHhKAzC40GyNLIoipzESo9g8N93eYoaGBvNtTVHcB93UAsGvwPbuAKTxK-nLOmJy30Pw3_bEoN7QVQJD8SDP_tq_URCqLPJbwHLGqsTgmjhb0jGGUIlHOJxcN6O31VTxRu06owiKjz0pGgBpi52V76mmaAsURlxmawQYVvq3pUXyn2KP0WVf7b_p7aiZxQxIGaU6OJ2Kftu0Pp5699XzojgBr5M9N14JRXAGGFE=w1366-h657" />

## Usage:

Just run ```draw.py```:
```
$ python draw.py
```
- <b>Now draw your digits and press ENTER to classify </b>
- Press Esc to exit the app.

## File Descriptions:
- ```train.py``` is consist of our model (loading and preprocess dataset, training the model and save the model in ```mnist_cnn.h5``` file)
- ```preprocessors.py``` is consist of 3 functions that is used in ```predictions.py``` for preprocess the drawn digits.
- ```predictions.py``` is consist of 2 functions that is used to get predictions for each digit.
- ```draw.py``` is our GUI for drawing digits and viewing our result.

## Note:
The tensorflow model that I used is a simple CNN model. The model is defined in ``` train.py ``` file. Try your preferred model and see how it performs!

The default model:

<img src="https://lh3.googleusercontent.com/fife/AAbDypD9kZgzJqfR6IIb4g9JFzhtJS2HYI_cZRBhdZvgklgP3Vco31Y05YdT-FqZ_TUNHb3ZFiCmoiCaoDdFAUkZf3qNkpHGqkllpmvbKF2etzco5eboYsnqEjq3fx6B_jMtVfHHigWeXlDigCkXXnlMhP0J-YaruAqU5vAyMQVjr73IL1YUXzFD3km0eZwXyKwbDMJJPlYlfYc0tq__E6MINEL1ffMACTiHBXY2m1bx9XGD23wX09CN0dK_635krXvvBQZd4nzTHIJBItXRLA9Vekq6SbdQ7irtj6H5Aqr3u57vfLw5AxD-wGI0-RuJASP9QwSQSYfNNDYXlAxIJevtRBt8VdoA_IpX8hxBgwKacl8cLXU4wsumw4RTt3LC7PXc8FRTzWlqS5j4Z6LCgcs26dtnycB5QPLAGdqB_P2HeVo-4Rtda2efbYZr3Q9xpGjnBwVItBvLnKD7TKD9tyGSr3MWOjQ-CmGfqhof7gahBirm5UsKGIoyL6o1V5sI6-lrAKZVD5X8P9ccbC9JPpLTwc5MYh-A_tfc-lrOYt7s04RazRtOVRiJfEfCjSpnxeeT1uWmsVrRvgxamD1Dbxy0tYcrojhZuDEKi-HzVBRzR11_NdM9aY_YGMMFI-rtY6cdKS_f7HZCyMCX1CApxOlLZZFJyukdc1b5JcpetD1vonrHjl0eGeo9_FHkaYsZQwmjUh1y9ogqrBjCeuxdKCaWGgzPMoQZFRhGI3TsIYk9av7wWWBBiPjbXzDd_Z-YXQ-Germfb_spve1EMERJNG5RhR4whOHDCn6nhCeRfwUabc-zVdrdK2t2R7U-OJBSNfJcfEZGxzvkreQYc6Zv8PWt9cGIx-gYw42v8MA1cLDvdRSlE63sYjs0UV38eAzo2ekZN5dTH1VC0SQSZQaH-kHmIEUZuKTY2djnXpKLsQtanJPfSQTqOx2Ds1VWOeCPqplMjrT93vhejoDFQnTTQ5pjGdkU6rMIdccswHcD-FZLWMPgogg-Lv0rTMYgqxw56isSljvSElQJToKopaSJdb6JuEQEpDHRgGjRkxsgiP0sY2tZBKJIArShw9Om6ohSYrr_J0zxPIDmuqr0GuzSWl7zO8xOjnAnpxy3_dnTngrHHD7gW01vKlROOe1xnFQp4PzIUOqF0a4DSS9FDvq2njfmA3JGzHtd8Xl8Pxh1vHeSs9UTPJYyYyyqIrZ5EEuhCIk7w4KSOS8G4zWnW4VE5811VcuTlWgU4Z2RPZGQrOeV4HLWKjciVIQC9Vg76IynMTh1S6I9oUE=w1366-h600"/>


