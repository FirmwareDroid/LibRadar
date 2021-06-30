# LibRadar - Fork for FirmwareDroid
LibRadar is an automatic tool for Android library detection. Upload your apk file and LibRadar can detect third-party 
libraries in Android apps accurately and instantly. Since the original repository is outdated this repo 
contains an updated version of LibRadar for Python-3.

## Features

#### Fast
LibRadar takes just several seconds to scan an app and report the list of third-party libraries used in it.
#### Accurate
LibRadar is trained with more than 1 million apps from Google Play, so it can identify virtually all popular libraries in any given Android app.
#### Anti-Obfuscation
Many Android apps are obfuscated with tools such as ProGuard, which makes it difficult to recognize a library by its package names or class names.
LibRadar is obfuscation-resilient since we use features that cannot be obfuscated, such as statistics on Android APIs.

## Usage

```bash
$ python LibRadar/libradar.py someapp.apk
```
View [docs/QuickStart.md](https://github.com/pkumza/LibRadar/blob/master/docs/QuickStart.md) for more information.

If you want an online trial, just click http://radar.pkuos.org/. (Updated to  version 2)

## Description for output
|V2|V1|Stands for|Description|
|---|---|---|---|
|Library|lib|Library|Library Name|
|Package|cpn|Current Package Name|The package name from **your given APK** that seems match this library. 'Current' means what you just uploaded.|
|Permissions|p|Permission|The permissions that the library used. It is specified by the API it used.|
|Popularity|dn|Repetitions|The number of the library (of just the **same version**!)|
|Match Ratio|*Not Implemented*|Similarity|Matched Parts/Total Parts|
|Standard Package|pn|Package Name|The package name from the database that seems matched.|
|Type|tp|Type|The type that the library belongs to.|
|Website|ch|Link| Link for the official SDK developer guide website. I forget why I used 'ch' at the very beginning.|
|*Not Implemented*|bh|B\_Hash|The hash value of the package.|
|*Not Implemented*|btc|B\_Total\_Count|The total count of API.|
|*Not Implemented*|btn|B\_Total\_Number|The total types of API.|
|*Not Implemented*|csp|Current Specified Package Name|The sub-package (a part of the whole package) from your given APK that finally, exactly matched with what in the database.|
|*Not Implemented*|sp|Specified Package Name|The sub-package(a part of the whole package) that exactly matched with that in your APK.|

