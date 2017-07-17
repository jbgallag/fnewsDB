

open(FILE, "$ARGV[0]");

while(<FILE>) {
   $_ =~ tr/\n//d;
   @data = split(/\t/, $_);
   if($data[0] !~ /Comics/) {
      @name = split(/\s+/, $data[1]);
      for($i=0; $i<=$#name; $i++) {
         $revName = join' ',$revName,$name[$#name-$i];
      }
      $revName =~ s/^\s+//g;

   print "$data[0]	$revName	$data[2]	School Paper	$data[3]	$data[4]	$data[5]	$data[6]\n";
   $revName = '';
   }

}
