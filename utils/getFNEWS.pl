%months = ("January", 1, "February", 2, "March", 3, "April", 4, "May", 5, "June", 6, "July", 7, "August", 8, "September", 9, "October", 10, "November", 11, "December", 12);
open(FILE, "$ARGV[0]");
open(OUT, ">$ARGV[1]");
while(<FILE>) {
   $_ =~ tr/\n//d;
   `wget $_`;

   `grep h2 index.html |grep http >>linksdata`;

   @nextPage = `grep "next page" index.html`;
   @npData = split(/\"/, $nextPage[0]);
   $count = 1;
   while($npData[3] ne '') {
        `wget $npData[3]`;
        $indexFile = "index.html"."\."."$count";
        `grep h2 $indexFile |grep http >>linksdata`;
	$count++;
        @nextPage = `grep "next page" $indexFile`;
        @npData = split(/\"/, $nextPage[0]);
    }
   open(DATA, "linksdata"); 
   @links = <DATA>;
   close(DATA);
   `rm index.html*`;
   `rm linksdata`;
   foreach $link (@links) {
     $link =~ tr/\n//d;
     @ldata = split(/\>/, $link);
     @urlData = split(/\"/, $ldata[1]);
     @titleData = split(/\</, $ldata[2]);
 
     `wget $urlData[1]`;
     @name = `grep "Posts by" index.html`;
     @nameData = split(/\>/, $name[0]);
     @authorData = split(/\</, $nameData[1]);

     @date = `grep -A1 clock index.html`;
     $date[1] =~ s/^\s+//g;
     @dateData = split(/\</, $date[1]);
     @spD = split(/\s+/, $dateData[0]);
     $month = $months{$spD[0]};
     $month = sprintf("%02d", $month);
     $day = sprintf("%02d", $spD[1]);
     $fullDate = "$spD[2]"."-"."$month"."-"."$day";

     @cat = `grep "category tag" index.html`;
     @catData = split(/\>/ , $cat[0]);
     @catg = split(/\</, $catData[1]);
     `rm index.html`;
     print OUT "$titleData[0]::$authorData[0]::$fullDate::$catg[0]::$urlData[1]\n";
     }
}

close(OUT);
close(FILE);
     
