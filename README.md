<!-- PROJECT SHIELDS -->
[![Build Status][build-shield]]()
[![Contributors][contributors-shield]]()



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hohohoesmad/PrxGetter/">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">PrxGetter</h3>

  <p align="center">
    This is an awesome tool to scrape and check proxies. 
    <br />
    <br />
    <a href="https://github.com/hohohoesmad/PrxGetter/issues">Report Bug / Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Contributing](#contributing)

<!-- ABOUT THE PROJECT -->
## About The Project

This project was built with the purpose of saving time when searching for proxies.
ALSO: Support for Python 3 has been dropped.

<!-- GETTING STARTED -->
## Getting Started

You dont need major knowledge the script does everything for you :)
Just download and enjoy.

### Prerequisites

There are 2 Python Packages needed for this script:
* bs4 (BeautifulSoup)
* requests (Requests)

## Usage
***MODES:***<br>
* 1: Scrapes and checks proxies from HTTPTunnel.ge.<br>
* 2: Tries to scrape and check proxies from a given source.<br>
* 3: Checks proxies from a given file.<br>
***ARGUMENTS:***<br>
* -1 (Sets the mode to 1) -- Mode 1 does not require additional arguments.<br>
* -2 (Sets the mode to 2)<br>
***Additional arguments:***<br>
  The source URL to scrape the proxies from. (No '-' required)<br>
* -3 (Sets the mode to 3)<br>
***Additional arguments:***<br>
  The source file to check the proxies from. (No '-' required)<br>
* -p (Prints the progress of the proxie checking) -- OPTIONAL<br>
***EXAMPLES OF USE:***<br>
Example 1 :<br>
> python PrxGetter.py -1<br>
Doing this will only scrape and check the proxies from the original URL (HTTPTunnel.ge)<br>
Example 2 :<br>
> python PrxGetter.py -2 http://pagefullofproxies.com -p<br>
Doing this will try to scrape the proxies from <<pagefullofproxies.com>> and print the progress.<br>

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
