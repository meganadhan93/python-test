while IFS= read -r dirname
do
	echo $dirname
	      appname=$dirname

	         if [[ -d $appname ]] ; then
		 echo "appname $appname will be used for dir change"
	         #cd $appname
			         # ./viktor-cli ci-install
				   #  ./viktor-cli ci-test
				         else  
						     echo "appname $appname will be ignored"  
						        # pwd
							    # ls -al
							                                   
							         fi     
done < dirname.txt

#
