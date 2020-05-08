---
layout: default
title: Home
nav_order: 1
description: "The main page for pandoru"
permalink: /
---

# Installation
{: .fs-9 }

Pandoru gives you an easy way to create and manage your Flask applications. 
{: .fs-6 .fw-300 }

[Get started now](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [View it on GitHub](https://github.com/polowis/Pandoru_template){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Getting started

### Dependencies

Pandoru uses Python 3 as its main version. Pandoru requires no other extensions, everything you need to packaged inside Pandoru. It also does not depend heavily on other libraries. 

Make sure you have satisfied these requirements
1. Python >= 3.6+
2. Database setup (sqlite, mysql, postgresql, etc.)
3. NodeJS >= 11
4. Redis

##### Optional dependencies
```webdriver``` - required if you want to run ```flask test``` command. Or you can just remove the folder that requires ```selenium``` which can be found at ```app/test/browser```

### Install Pandoru 

1. To install Pandoru, fork the sources. 

2. Open your terminal and ```cd``` to your ```~/your_folder``` folder

3. Clone your fork into the ~/your_folder folder, by running the following command replace your username into {your_username} slot:
```sh
$ git clone git@github.com:{your_username}/Pandoru_template
```

4. ```cd``` to the new directory you just created
```sh
$ cd Pandoru_template
```

5. Run the ```install.sh```bin script
If your machine has satisfied with all the requirements listed above, skip this step

```sh
$ ./bin/install.sh
```

6. Run ```setup.sh``` bin script. If you already run the ```install.sh``` script, skip this step
```sh
$ ./bin/setup.sh
```