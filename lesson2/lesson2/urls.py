"""lesson2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse, response
from django.contrib import admin
from django.urls import path

def appsum(request):
    a=request.GET.get('a') 
    b=request.GET.get('b')
    sum=int(a)+int(b)
    return HttpResponse(f"<h1 style='text-align:center;background-color: gray;'>SUM = {sum}</h1>")

def index(request):
    html="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
    *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    list-style: none;
    text-decoration: none;
    
    color: white;
    font-family:Georgia, 'Times New Roman', Times, serif;
    font-weight: bold;
}
body{
    background-color: grey;
    
}
.header{
    width: 90%;
    height: 140px;
    margin: 0 auto;
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;

}

.navbar{
    width: 400px;
    height: 120px;
}
.navbar ul {
    width: 250px;
    height: 120px;
    margin: 0 auto;
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-around;
    align-items: center;
    padding:0;

}
.navbar ul li{
    padding: 6px 7px;
    border-radius: 3px;
    margin: 0 7px;
}
.navbar ul li:hover{
    background-color: darkorange;
    
    
}
.navbar a{
    font-weight: bold;
    
}
.navbar a:hover{
    color: black;
    opacity: 0.6;
}
.active{
    background-color: darkorange;

}
    </style>
    <title>Index</title>
</head>
<body>
    <div class="header">
        <h1>TETRATEX MCHJ</h1>
        <div class="navbar">
            <ul>
                <li class="active"><a href="#">HOME</a></li>
                <li><a href="#">PROJECT</a></li>
                <li><a href="#">CONTACT</a></li>
            </ul>
        </div>
    </div>
    
</body>
</html>
    """
    return HttpResponse(html)    



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/',appsum),
    path('',index)
]
