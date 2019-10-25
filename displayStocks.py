import redis
import random
import string
import os
import cherrypy
from os.path import abspath
import json

redis_host = "localhost"
redis_port = 6379
redis_password = ""

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


class StringGenerator(object):
    
    # 1) Gets the code of stocks  from redis in descending order
    # 2) Getting all the stocks info from redis and storing it in an array
    # 3) Looping through the array populating the html table with the top 10 stocks
    @cherrypy.expose
    def index(self):
        li = r.zrevrange("equity", 0, 9)
        
        # below commented code just populates data with dummy values
        '''li = []
        for i in range(10):
            d = {}
            d["name"] = i
            d["open"] = 10 + i
            d["high"] = i   
            d["low"] = i    
            d["close"] = i

            json_data = json.dumps(d)

            li.append(json_data)'''
        
        lis = []

        for i in li:
            lis.append(json.loads(r.get(r.get(i))))

        # below commented code just populates data with dummy values
        '''for i in li:
            lis.append(json.loads(i))'''

        return"""<html>
          <head>
              
              <style>
                    p{{
                        font-family: Lato-Bold;
                        margin-left:45%;
                       
                    }}
                    input[type=text] {{
                        margin-left:64%;
                        border: 1px solid #ccc;  
                    }}
                    
                    table {{
                        width:70%; 
                        margin-left:15%; 
                        margin-right:15%;
                        font-family: arial, sans-serif;
                        border-collapse: collapse;
                        
                        border-radius: 10px;
                    }}

                    th {{
                        
                        font-family: Lato-Bold;
                        font-size: 15px;
                        color: #00ad5f;
                        line-height: 2;
                        text-transform: uppercase;
                        background-color: #393939;
                        
                    }}

                    .name{{
                    padding-left: 10px;
                    }}
                    
                    td{{
                    
                        font-family: Lato-Regular;
                        font-size: 15px;
                        color: #808080;
                        line-height: 1.4;
                        background-color: #222222;

                        padding-left: 70px;
                        padding-right: 20px;
                        padding-top: 10px;
                        padding-bottom: 10px;
                    }}
              </style>
          </head>
          <body>
              <p>Top 10 Stocks for today</p>
              <form method="get" action="search">
                  <input type="text" name="stock" placeholder="Search.."/>
                  <button type="submit">Search</button>
            </form>
              <table id ="stocks">
                  <tr>
                      <th class = "name">Name</th>
                      <th>Open</th>
                      <th>High</th>
                      <th>Low</th>
                      <th>Close</th>
                      
                  </tr>
                
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
                  <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                  </tr>
              </table>
              
              <script>
                  var arr = {a};

                  for(var i = 0; i < 10; i++){{
                      console.log(arr[i]["open"]);
                      console.log(arr[i]["name"])
                  }}

                  for(var i = 1; i <= 10; i++){{
                      document.getElementById("stocks").rows[i].cells[0].innerHTML = arr[i-1]["name"];
                      document.getElementById("stocks").rows[i].cells[1].innerHTML = arr[i-1]["open"];
                      document.getElementById("stocks").rows[i].cells[2].innerHTML = arr[i-1]["high"];
                      document.getElementById("stocks").rows[i].cells[3].innerHTML = arr[i-1]["low"];
                      document.getElementById("stocks").rows[i].cells[4].innerHTML = arr[i-1]["close"];
                  }}
                  
              </script>  
         </body>
        </html>""".format(a = lis)

    # 1) given the name of a stock convert it to uppercase
    # 2) if the name is present in the db then render a simle html table showing the details of the stock
    # 3) if it is not in the db then render an html page allowing the user to be able to return back to the home screen
    @cherrypy.expose
    def search(self, stocks):
        a = stocks.strip().upper()
        
        try:
            jsonObject = json.loads(r.get(str(a)))
        
            return"""<html>
              <head>
                  <style>
                      table {{
                            width:70%; 
                            margin-left:15%; 
                            margin-right:15%;
                            font-family: arial, sans-serif;
                            border-collapse: collapse;
                        
                            border-radius: 10px;
                        }}

                        th {{
                        
                            font-family: Lato-Bold;
                            font-size: 15px;
                            color: #00ad5f;
                            line-height: 2;
                            text-transform: uppercase;
                            background-color: #393939;
                        
                        }}

                        .name{{
                        padding-left: 10px;
                        }}
                    
                        td{{
                    
                            font-family: Lato-Regular;
                            font-size: 15px;
                            color: #808080;
                            line-height: 1.4;
                            background-color: #222222;

                            padding-left: 70px;
                            padding-top: 10px;
                            padding-bottom: 10px;
                        }}
                  </style>
              </head>
              <body>
                  <form method="get" action="index">
                      <button type="submit">Previous page</button>
                  </form>
            
                  <table>
                      <tr>
                          <th class = "name">Name</th>
                          <th>Open</th>
                          <th>High</th>
                          <th>Low</th>
                          <th>Close</th>
                      
                      </tr>
                      <tr>
                          <td>{}</td>
                          <td>{}</td>
                          <td>{}</td>
                          <td>{}</td>
                          <td>{}</td>
                      </tr>
                  </table>
             </body>
            </html>""".format(jsonObject["name"], jsonObject["open"],jsonObject["high"], jsonObject["low"],jsonObject["close"])

        except:
            return """<html>
                  <head>
                      <style>
                          p{{
                              font-family: Lato-Bold;
                              padding-left: 70px;
                          }}

                          button{{
                             margin-left:40%;
                          }}
                          
                      </style>
                  </head>
                    <body>
                      <p>OOps could not find the stock please try again</p>
                      
                      <form method="get" action="index">
                          <button type="submit">Previous page</button>
                      </form>
            
                   </body>
                </html>"""

if __name__ == '__main__':

    cherrypy.quickstart(StringGenerator(), '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})

    



















    
