<div align="center">
   <img src="https://blog.bag-xml.com/amber/static/resources/vine-x-tweak.png" height="160" width="160">
   <h1>VineX</h1>
</div>

A server made for older versions of the iOS Vine application.

## Information and Compatibility
VineX is primarily made for the Vine iOS app, version 1.1.2. It's recommended that on release, VineX may only be used with that specific version, as support for more versions will be added in the future.

This is just a flask server, therefore should then be familiar for people who've worked with flask before.

VineX will come with a tweak too, which'll support the following iOS versions:

| iOS Version  | Support status |
| ------------- | ------------- |
| iOS 5  | Not supported  |
| iOS 6  | Supported  |
| iOS 7  | Supported  |
| iOS 8  | Supported  |
| iOS 9  | Supported  |
| iOS 10  | Untested  |
| iOS 11  | Untested  |

## Roadmap
Here is a table to show what endpoints have been implemented into VineX. And what features are still due to add.

| Authentication endpoints  | Context | Status |
| ------------- | ------------- | ------------- |
| /users  | Registration  | Completed  |
| /users/authenticate [POST] | Login  | Completed  |
| /users/authenticate [DELETE]  | Log-Out  | Completed  |
| /users/forgotPassword  | Password reset  | Incomplete  |

| User Endpoints  | Context | Status |
| ------------- | ------------- | ------------- |
| /users/profiles/(User-ID)  | User Profile  | Completed  |
| /users/me | Userinfo retrieval  | Completed(?)  |
| /users/(User-ID)  | Settings management  | Completed  |
| /users/(User-ID)/preferences  | Settings management  | Completed  |
| /users/(User-ID)/pendingNotificationsCount  | Notification indicator  | Being worked on  |
| /users/(User-ID)/notifications  | Notifications (Activity page)  | Being worked on  |
| /users/(User-ID)/following  | Following Page  | Being worked on  |
| /users/search/(Search query)  | User search  | Incomplete  |
| /users/(User-ID)/followers [GET]  | Follower Page  | Being worked on  |
| /users/(User-ID)/followers [POST]  | Follow a user  | Completed  |
| /users/(User-ID)/followers [DELETE]  | Unfollow a user  | Completed  |
| /users/(User-ID)/blocked/(Target-User-ID) [POST]  | Block a user  | Completed  |
| /users/(User-ID)/blocked/(Target-User-ID) [DELETE]  | Unblock a user  | Completed  |
| /users/(User-ID)/complaints/  | File a complaint  | Being worked on  |
| /users/(User-ID)/following/suggested/contacts  | Address Book integration  | Complete  |


| Timeline  | Context | Status |
| ------------- | ------------- | ------------- |

| Explore  | Context | Status |
| ------------- | ------------- | ------------- |
| /explore/(app version)  | Explore page  | Incomplete  |

| Tags  | Context | Status |
| ------------- | ------------- | ------------- |
| /tags/search/(Search query)  | Hashtag search  | Incomplete  |

## Bugs
Improper saving to the MySQL Database

## How to use?
You need to install python, then just install the requirements.
Requirements for this project are:

flask
other
