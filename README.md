# adidas-account-generator

An Adidas.com account generator that creates accounts without requiring a captcha harvester of any sort (manual captcha harvesting, 2captcha, or anti-captcha).
* Exports account info to a .txt file ```createdaccounts.txt```
* NOTE: This currently kinda-supports proxies. The code is there for proxy and threading but it's still buggy and in development. Feel free to contribute. If you put proxies into the file it will automatically use them and start threading.
* Proxies can be ip or user/pass verified.
* Uses gmail dot trick - ```example@gmail.com == e.x.ample@gmail.com == e.x.a.m.p.l.e@gmail.com == examp.l.e@gmail.com``` and so on.
* You can create 2*(n-1) unique accounts where n equals the amount of charachters you have in your email.
* Base email addresses must not have dots in them already.
![](https://github.com/antonjlin/adidas-account-generator/blob/master/Screen%20Shot%202018-01-02%20at%2011.51.38%20PM.png)
## Make login links
* To make login links, copy and paste this link into your browser.
```
https://cp.adidas.com/idp/startSSO.ping?username=[MYEMAIL]&password=[MYPASSWORD]&signinSubmit=Sign+in&IdpAdapterId=adidasIdP10&SpSessionAuthnAdapterId=https%3A%2F%2Fcp.adidas.com%2Fweb%2F&PartnerSpId=sp%3Ademandware&validator_id=adieComDWgb&TargetResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2FMyAccount-ResumeLogin&target=account&InErrorResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2Fnull&loginUrl=https%3A%2F%2Fcp.adidas.com%2Fweb%2FeCom%2Fen_US%2Floadsignin&cd=eCom%7Cen_US%7Ccp.adidas.com%7Cnull&remembermeParam=&app=eCom&locale=US&domain=cp.adidas.com&pfRedirectBaseURL_test=https%3A%2F%2Fcp.adidas.com&pfStartSSOURL_test=https%3A%2F%2Fcp.adidas.com%2Fidp%2FstartSSO.ping%3F&resumeURL_test=&FromFinishRegistraion=&CSRFToken=null
  ```
* Replace ```[MYEMAIL]``` with your email and ```[MYPASSWORD]``` with your password.
* The page should automatically log you into the account.

### TO USE THIS SCRIPT:
Install the latest version of python. This only works on python 3+
1. Clone the repository or download and extract thezip
2. install the dependencies
```
pip3 install requests
pip3 install bs4
```
4. cd into the folder you cloned the repo in. 
```
cd documents/github/adidas-account-tester (or whatever directory you downloaded this folder to)
python3 accountgen.py
```

## ToDo
- [X] Account creation
- [X] Threading and proxies (kinda there, but use at your own risk)
- [ ] Support for different regions (EU, UK, GE)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Credit
* Made by [Anton Lin](https://github.com/user/antonjlin)
* Feel free to contribute to this and submit a pull request
