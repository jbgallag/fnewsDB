#!/usr/bin/perl

chdir("/Users/jbgallag/fnews_06272017/fnews_work");
$baseUrl = "http://fnewsmagazine.com/";

if($ARGV[0] eq "") {
   $year = `date +%Y`;
   chop($year);
   $month = `date +%m`;
   chop($month);
   $url = "$baseUrl"."$year"."/"."$month"."/";
} else {
   $url = "$baseUrl"."$ARGV[0]";
}


open(OUT, ">url.dat");
print OUT "$url\n";
close(OUT);

`perl getFNEWS.pl url.dat fnews_download.dat`;
`perl fixdb.pl fnews_download.dat > fnewsRevNames.dat`;
`perl getAuthor.pl fnewsRevNames.dat > authList`;
`python inputAuthors.py authList`;
`python inputFNEWSArticles.py fnewsRevNames.dat`; 

`rm -f url.dat fnews_download.dat fnewsRevNames.dat authList`;
