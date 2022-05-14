# Web-Proxy

# Instruction for running: 
To run ProxyServer, first you need to go to file  directory in command prompt and then run following in command prompt. </br>
python ProxyServerMultiClient.py 127.0.0.1 </br>
python ProxyServerSingleClient.py 127.0.0.1 </br>

From web browser you can request particular page in this format. </br>
127.0.0.1:8888/yahoo.com
Anytime you can see the ‘log.txt’ to observe cache resources. </br>

# Execution sample: 
Initially log file looks like.

<img width="417" alt="image" src="https://user-images.githubusercontent.com/15192980/168447040-d2b6f50d-7f02-440a-8690-071e7fa74a01.png">

After running ProxyServerMultiClient.py and request my.utep.edu at browser.

<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447050-5b45a235-37dd-4630-9fa3-57238eba793d.png">
 
<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447057-17a4c291-c422-4174-aa9c-f94370540ac0.png">

<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447061-1152e56d-88df-469e-b1fb-0aabb4b66140.png">

Log.txt now.

<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447073-9858e5cf-7971-4f9a-8348-2ff70154d4cd.png">

Because of multithreading, sometime printing statements are not in particular order. That’s why I also provide ProxyServerSingleClient.py file. if you run it for yahoo.com , will see following output.

<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447110-817137c0-e029-4976-8b0b-43eb339b2528.png">


Again when you request for yahoo.com.

<img width="432" alt="image" src="https://user-images.githubusercontent.com/15192980/168447115-af98d926-3356-412e-9813-dbdafbac6f47.png">

 
 
