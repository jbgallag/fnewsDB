

open(FILE, "$ARGV[0]");

while(<FILE>) {
   $_ =~ tr/\n//d;
   @data = split(/::/, $_);
   @name = split(/\s+/, $data[1]);
   for($i=0; $i<=$#name; $i++) {
     $revName = join' ',$revName,$name[$#name-$i];
   }
   $revName =~ s/^\s+//g;

   print "$data[0]::$revName::$data[2]::School Paper::$data[3]::$data[4]\n";
   $revName = '';

}
