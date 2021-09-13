# FILE SYSTEM 

So, the main purpose of this project is practice to create and deploy API on several servers.

Practice Ideas:
- VPN
- A subnet simulator
- Network load balancing System
- File Transfer Protocol
- data server, like [file-transfer](https://github.com/f1le-transfer) but simpler

And I decided to create a simplified multi-user file system. I'm not going to make a full-fledged file system considering all the little things, roughly speaking, this is a mock-up to try working with several servers. In the course of the development of the system, I will explain below what can be improved to make the system better.

# What needs to be improved
- add system of API keys
- make all operations atomic
- Chunking Files. Instead of uploading entire file in one go, chunking files in blocks and then uploading each chunk.
- Make full authorization and authentication, since now passwords are simply stored in dB without processing.
