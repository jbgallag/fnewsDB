$baseDir = "/Users/jbgallag/fnews_06272017/fnews_work";
$wget = "/usr/local/bin/wget";
%months = ("January", 1, "February", 2, "March", 3, "April", 4, "May", 5, "June", 6, "July", 7, "August", 8, "September", 9, "October", 10, "November", 11, "December", 12);
open(FILE, "$ARGV[0]");
open(OUT, ">$ARGV[1]");
while(<FILE>) {
   $_ =~ tr/\n//d;
   `$wget $_ -O $baseDir/index.html`;

   `grep h2 $baseDir/index.html |grep http >>$baseDir//linksdata`;

   @nextPage = `grep "next page" $baseDir/index.html`;
   @npData = split(/\"/, $nextPage[0]);
   $count = 1;
   while($npData[3] ne '') {
	$outfile = "index.html"."\."."$count";
        `$wget $npData[3] -O $baseDir/$outfile`;
        $indexFile = "$baseDir/"."index.html"."\."."$count";
        `grep h2 $indexFile |grep http >>$baseDir/linksdata`;
	$count++;
        @nextPage = `grep "next page" $indexFile`;
        @npData = split(/\"/, $nextPage[0]);
    }
   open(DATA, "linksdata"); 
   @links = <DATA>;
   close(DATA);
   `rm $baseDir/index.html*`;
   `rm $baseDir/linksdata`;
   foreach $link (@links) {
     $link =~ tr/\n//d;
     @ldata = split(/\>/, $link);
     @urlData = split(/\"/, $ldata[1]);
     @titleData = split(/\</, $ldata[2]);
 
     `$wget $urlData[1] -O $baseDir/index.html`;
     #parse author
     @name = `grep "Posts by" index.html`;
     @nameData = split(/\>/, $name[0]);
     @authorData = split(/\</, $nameData[1]);
     
     #parse date
     @date = `grep -A1 clock index.html`;
     $date[1] =~ s/^\s+//g;
     @dateData = split(/\</, $date[1]);
     @spD = split(/\s+/, $dateData[0]);
     $month = $months{$spD[0]};
     $month = sprintf("%02d", $month);
     $day = sprintf("%02d", $spD[1]);
     $fullDate = "$spD[2]"."-"."$month"."-"."$day";
     
     #parse category
     @cat = `grep "category tag" $baseDir/index.html`;
     @catData = split(/\>/ , $cat[0]);
     @catg = split(/\</, $catData[1]);
    
     #parse illustrations 
     @ills = `grep -i "illustration by" $baseDir/index.html`;
     @illsData = split(/\</, $ills[0]);
     @imgUrl = split(/\"/, $illsData[2]);
     $img = $imgUrl[3];
     @illData = split(/\>/, $illsData[3]);
     @illAuth = split(/\s/, $illData[1]);
     $revName = "";
     for($i=0; $i<$#illAuth; $i++) {
	if($illAuth[$#illAuth-$i] !~ /illustration/ && $illAuth[$#illAuth-$i] !~ /Illustration/ &&
           $illAuth[$#illAuth-$i] !~ /by/ && $illAuth[$#illAuth-$i] !~ /By/) {
		$illAuth[$#illAuth-$i] =~ s/[[:punct:]]//g;
        	$revName = join" ",$revName,$illAuth[$#illAuth-$i];
	}
     }
     $revName =~ s/^\s+//g;
     `rm $baseDir/index.html`;
     if($img ne '') {
     	print OUT "$titleData[0]	$authorData[0]	$fullDate	$catg[0]	$urlData[1]	$img	$revName\n";
	} else {
     	print OUT "$titleData[0]	$authorData[0]	$fullDate	$catg[0]	$urlData[1]	None	None\n";
        }
     }
}

close(OUT);
close(FILE);
     
