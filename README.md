# Yelp-scraper-webapp

![Capture d’écran 2021-09-15 à 17 02 09](https://user-images.githubusercontent.com/83681204/133468776-bae63ce1-7e78-4e35-a14d-f5f329d8098b.jpg)


<hr>
<br>
Yelp scraper is a simple web application that can run on your computer, it's used to collect business and consumers reviews data for yelp website, it's built using SELENIUM and Flask and provide the following informations in csv file :

<br>
<ul>
  <li>business name</li>
  <li>business website</li>
  <li>business phone</li>
  <li>business features</li>
  <li>business work_hours</li>
  <li>number of consumers reviews</li>
  <li>business rating</li>
  <li>business url in yelp website</li>
  
</ul>
<br>
To use the web app you need to :
<br>
Install some libraries in your terminal/cmd: <h3>pip install selenium pandas parsel Flask</h3>
<br>

Excute the command in the terminal/cmd : 
<h3>cd yelp</h3>
<h3>python app.py</h3>

<br>
You will get a simple page with 3 inputs:
<ul>
  <li>business type : like Restaurents, accountants, coffee...) </li>
  <li>business location : the area to search in </li>
  <li>number of pages : the number of pages to be collected from yelp website</li>
</ul>

<br>

After you submit the data will be saved in csv format in the yelp directory




