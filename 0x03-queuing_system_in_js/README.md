## Queuing System in JS
![image](https://github.com/Smambo/alx-backend/assets/113464914/e58da519-9a48-44aa-99b4-407cce0f3d92)

### Learning Objectives:
* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

### Requirements
* All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
* All of your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `js` extension

### Required files for the project:
* [package.json](./package.json)
* [.babelrc](./.babelrc)

<b>and...</b>
Don't forget to run `$ npm install` when you have `package.json`

### Tasks:
### [0. Install a redis instance](./README.md)<br>
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/downloads/](./https://redis.io/downloads/)):

```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

* Start Redis in the background with `src/redis-server`

```
$ src/redis-server &
```

* Make sure that the server is working with a ping `src/redis-cli ping`

```
PONG
```

* Using the Redis client again, set the value `School` for the key `Holberton`

```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

* Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```
$ kill [PID_OF_Redis_Server]
```

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:

* Running `get Holberton` in the client, should return `School`

### [1. Node Redis Client](./0-redis_client.js)<br>
Install [node_redis](./https://github.com/redis/node-redis) using npm

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

* It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
* It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

<b>Requirements:</b>

* To import the library, you need to use the keyword `import`

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# ps aux | grep redis-server
root     21240  0.0  0.0  13140   932 pts/2    S+   16:36   0:00 grep --color=auto redis-server
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# redis-6.0.10/src/redis-server > /dev/null 2>&1 &
[1] 21500
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# ps aux | grep redis-server
root     21500  0.1  0.0  61320  5060 pts/2    Sl   17:17   0:00 redis-6.0.10/src/redis-server *:6379
root     21506  0.0  0.0  13140  1072 pts/2    S+   17:17   0:00 grep --color=auto redis-server
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [2. Node Redis client and basic operations](./1-redis_op.js)<br>
In a file `1-redis_op.js`, copy the code you previously wrote (`0-redis_client.js`).

Add two functions:

* `setNewSchool`:
  * It accepts two arguments `schoolName`, and `value`.
  * It should set in Redis the value for the key `schoolName`
  * It should display a confirmation message using `redis.print`
* `displaySchoolValue`:
  * It accepts one argument `schoolName`.
  * It should log to the console the value for the key passed as argument

At the end of the file, call:

* `displaySchoolValue('Holberton');`
* `setNewSchool('HolbertonSanFrancisco', '100');`
* `displaySchoolValue('HolbertonSanFrancisco');`

<b>Requirements:</b>

* Use callbacks for any of the operation, we will look at async operations later

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 1-redis_op.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [3. Node Redis client and async operations](./2-redis_op_async.js)<br>
In a file `2-redis_op_async.js`, let’s copy the code from the previous exercise (`1-redis_op.js`)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async / await`

Same result as `1-redis_op.js`

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 2-redis_op_async.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [4. Node Redis client and advanced operations](./4-redis_advanced_op.js)<br>
In a file named `4-redis_advanced_op.js`, let’s use the client to store a hash value

### Create Hash:
Using `hset`, let’s store the following:

* The key of the hash should be `HolbertonSchools`
* It should have a value for:
  * `Portland=50`
  * `Seattle=80`
  * `New York=20`
  * `Bogota=20`
  * `Cali=40`
  * `Paris=2`
* Make sure you use `redis.print` for each `hset`
### Display Hash:
Using `hgetall`, display the object stored in Redis. It should return the following:

<b>Requirements:</b>

* Use callbacks for any of the operation, we will look at async operations later

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 4-redis_advanced_op.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [5. Node Redis client publisher and subscriber](./5-subscriber.js)<br>
In a file named `5-subscriber.js`, create a redis client:

* On connect, it should log the message `Redis client connected to the server`
* On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
* It should subscribe to the channel `holberton school channel`
* When it receives message on the channel `holberton school channel`, it should log the message to the console
* When the message is `KILL_SERVER`, it should unsubscribe and quit

In a file named `5-publisher.js`, create a redis client:

* On connect, it should log the message `Redis client connected to the server`
* On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
* Write a function named `publishMessage`:
  * It will take two arguments: `message` (string), and `time` (integer - in ms)
  * After `time` millisecond:
    * The function should log to the console `About to send MESSAGE`
    * The function should publish to the channel `holberton school channel`, the message passed in argument after the time passed in arguments
* At the end of the file, call:

```
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
```

<b>Requirements:</b>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time

<b>Terminal 1:</b>

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 5-subscriber.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
```

<b>Terminal 2:</b>

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 5-publisher.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

<b>And in the same time in Terminal 1:</b>

```
Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
Holberton Student #3 starts course
[nodemon] clean exit - waiting for changes before restart
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [6. Create the Job creator](./6-job_creator.js)<br>
In a file named `6-job_creator.js`:

* Create a queue with `Kue`
* Create an object containing the Job data with the following format:

```
{
  phoneNumber: string,
  message: string,
}
```

* Create a queue named `push_notification_code`, and create a job with the object created before
* When the job is created without error, log to the console `Notification job created: JOB ID`
* When the job is completed, log to the console `Notification job completed`
* When the job is failing, log to the console `Notification job failed`

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 6-job_creator.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1
^C
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the `JOB ID` increasing - it means you are storing new job to process…

### [7. Create the Job processor](./6-job_processor.js)<br>
In a file named `6-job_processor.js`:

* Create a queue with `Kue`
* Create a function named `sendNotification`:
  * It will take two arguments `phoneNumber` and `message`
  * It will log to the console `Sending notification to PHONE_NUMBER, with message: MESSAGE`
* Write the queue process that will listen to new jobs on `push_notification_code`:
  * Every new job should call the `sendNotification` function with the phone number and the message contained within the job data

<b>Requirements:</b>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time
* You muse use `Kue` to set up the queue

### [8. Track progress and errors with Kue: Create the Job creator](./7-job_creator.js)<br>
In a file named `7-job_creator.js`:

Create an array `jobs` with the following data inside:

```
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];
```

After this array created:

* Create a queue with `Kue`
* Write a loop that will go through the array `jobs` and for each object:
  * Create a new job to the queue `push_notification_code_2` with the current object
  * If there is no error, log to the console `Notification job created: JOB_ID`
  * On the job completion, log to the console `Notification job JOB_ID completed`
  * On the job failure, log to the console `Notification job JOB_ID failed: ERROR`
  * On the job progress, log to the console `Notification job JOB_ID PERCENTAGE% complete`

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# vi 7-job_creator.js
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 7-job_creator.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "7-job_creator.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 4
Notification job created: 5
Notification job created: 6
Notification job created: 7
Notification job created: 8
Notification job created: 9
Notification job created: 10
Notification job created: 11
Notification job created: 12
Notification job created: 13
Notification job created: 14
^Croot@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

### [9. Track progress and errors with Kue: Create the Job processor](./7-job_processor.js)<br>
In a file named `7-job_processor.js`:

Create an array that will contain the blacklisted phone numbers. Add in it `4153518780` and `4153518781` - these 2 numbers will be blacklisted by our jobs processor.

Create a function `sendNotification` that takes 4 arguments: `phoneNumber`, `message`, `job`, and `done`:

* When the function is called, track the progress of the `job` of `0` out of `100`
* If `phoneNumber` is included in the “blacklisted array”, fail the job with an `Error` object and the message: `Phone number PHONE_NUMBER is blacklisted`
* Otherwise:
  * Track the progress to 50%
  * Log to the console `Sending notification to PHONE_NUMBER, with message: MESSAGE`

Create a queue with `Kue` that will proceed job of the queue `push_notification_code_2` with two jobs at a time.

<b>Requirements:</b>

* You only need one Redis server to execute the program
* You will need to have two node processes to run each script at the same time
* You muse use `Kue` to set up the queue
* Executing the jobs list should log to the console the following:

<b>Terminal 2:</b>

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 7-job_processor.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "7-job_processor.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_processor.js`
Sending notification to 4153518743, with message: This is the code 4321 to verify your account
Sending notification to 4153538781, with message: This is the code 4562 to verify your account
Sending notification to 4153118782, with message: This is the code 4321 to verify your account
Sending notification to 4153718781, with message: This is the code 4562 to verify your account
Sending notification to 4159518782, with message: This is the code 4321 to verify your account
Sending notification to 4158718781, with message: This is the code 4562 to verify your account
Sending notification to 4153818782, with message: This is the code 4321 to verify your account
Sending notification to 4154318781, with message: This is the code 4562 to verify your account
Sending notification to 4151218782, with message: This is the code 4321 to verify your account
^Croot@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
```

<b>And in the same time in terminal 1:</b>

```
...
Notification job 26 0% complete
Notification job 27 0% complete
Notification job 26 failed: Phone number 4153518780 is blacklisted
Notification job 27 failed: Phone number 4153518781 is blacklisted
Notification job 28 0% complete
Notification job 29 0% complete
Notification job 28 50% complete
Notification job 28 completed
Notification job 29 50% complete
Notification job 29 completed
Notification job 30 0% complete
Notification job 31 0% complete
Notification job 30 50% complete
Notification job 31 50% complete
Notification job 30 completed
Notification job 31 completed
Notification job 32 0% complete
Notification job 33 0% complete
Notification job 32 50% complete
Notification job 33 50% complete
Notification job 32 completed
Notification job 33 completed
Notification job 34 0% complete
Notification job 35 0% complete
Notification job 34 50% complete
Notification job 35 50% complete
Notification job 34 completed
Notification job 35 completed
Notification job 36 0% complete
Notification job 36 50% complete
Notification job 36 completed
```

### [10. Writing the job creation function](./8-job.js)<br>
In a file named `8-job.js`, create a function named `createPushNotificationsJobs`:

* It takes into argument `jobs` (array of objects), and `queue` (`Kue` queue)
* If `jobs` is not an array, it should throw an `Error` with message: `Jobs is not an array`
* For each job in `jobs`, create a job in the queue `push_notification_code_3`
* When a job is created, it should log to the console `Notification job created: JOB_ID`
* When a job is complete, it should log to the console `Notification job JOB_ID completed`
* When a job is failed, it should log to the console `Notification job JOB_ID failed: ERROR`
* When a job is making progress, it should log to the console `Notification job JOB_ID PERCENT% complete`

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# cat 8-job-main.js
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
    }
];
createPushNotificationsJobs(list, queue);
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js#
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm run dev 8-job-main.js

> queuing_system_in_js@1.0.0 dev /alx-backend/0x03-queuing_system_in_js
> nodemon --exec babel-node --presets @babel/preset-env "8-job-main.js"

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 8-job-main.js`
Notification job created: 37
```

### [11. Writing the test for job creation](./8-job.test.js)<br>
Now that you created a job creator, let’s add tests:

* Import the function `createPushNotificationsJobs`
* Create a queue with `Kue`
* Write a test suite for the `createPushNotificationsJobs` function:
  * Use `queue.testMode` to validate which jobs are inside the queue
  * etc.

<b>Requirements:</b>

* Make sure to enter the test mode without processing the jobs before executing the tests
* Make sure to clear the queue and exit the test mode after executing the tests

```
root@088c4f11a28c:/alx-backend/0x03-queuing_system_in_js# npm test 8-job.test.js

> queuing_system_in_js@1.0.0 test /alx-backend/0x03-queuing_system_in_js
> mocha --require @babel/register --exit "8-job.test.js"



  createPushNotificationsJobs
    ✓ displays an error message if jobs is not an array
Notification job created: 38
Notification job created: 39
    ✓ adds jobs to the queue with the correct type (199ms)
Notification job 38 25% complete
    ✓ registers the progress event handler for a job
Notification job 38 failed: Failed to send
    ✓ registers the failed event handler for a job
Notification job 38 completed
    ✓ registers the complete event handler for a job


  5 passing (404ms)

```

### [12. In stock?](./9-stock.js)<br>
### Data
Create an array `listProducts` containing the list of the following products:

* Id: 1, name: `Suitcase 250`, price: 50, stock: 4
* Id: 2, name: `Suitcase 450`, price: 100, stock: 10
* Id: 3, name: `Suitcase 650`, price: 350, stock: 2
* Id: 4, name: `Suitcase 1050`, price: 550, stock: 5

### Data access
Create a function named `getItemById`:

* It will take `id` as argument
* It will return the item from `listProducts` with the same id

### Server
Create an `express` server listening on the port 1245. (You will start it via: `npm run dev 9-stock.js`)

### Products
Create the route `GET /list_products` that will return the list of every available product with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products ; echo ""
[{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}]
bob@dylan:~$ 
```

### In stock in Redis
Create a client to connect to the Redis server:

* Write a function `reserveStockById` that will take `itemId` and `stock` as arguments:
  * It will set in Redis the stock for the key `item.ITEM_ID`
* Write an async function `getCurrentReservedStockById`, that will take `itemId` as an argument:
  * It will return the reserved stock for a specific item

### Product detail
Create the route `GET /list_products/:itemId`, that will return the current product and the current available stock (by using `getCurrentReservedStockById`) with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
bob@dylan:~$ 
```

If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
```

### Reserve a product
Create the route `GET /reserve_product/:itemId`:

* If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
```

* If the item exists, it should check that there is at least one stock available. If not it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$ 
```

* If there is enough stock available, it should reserve one item (by using `reserveStockById`), and return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$ 
```

<b>Requirements:</b>

* Make sure to use `promisify` with Redis
* Make sure to use the `await/async` keyword to get the value from Redis
* Make sure the format returned by the web application is always JSON and not text

