Question_list = ["With which does the power to extend or restrict the jurisdiction of the High Court rest?",
"Gobar gas contains mainly which gas?",  
"Which is the biggest Public Sector undertaking in the country?", 
"Which rocks is transformed into marble?",
"Which Englishmen was fellow of Gandhiji in South Africa?",
"By which number the quality of gasolin sample is determined?",
"Due to bite of mad dog the disease hydrophobia is caused by which virus?",
"Who appoints the Chief Election Commissioner of India?",
"What is the principal reason for the formation of metamorphic rocks?",
"Who said I therefore want freedom immediately, this very night, before dawn if it can be had?",
"Grand Central Terminal Park Avenue New York is the world's",
"Entomology is the science that studies",
"Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
"Garampani sanctuary is located at",
"What is the cube root of 512"]

Option_list = [["1. With the Parliament", "2. With the Legislative", "3. With the Council of Minister", "4. With the Rajya Sabha"],
["1. Methane", "2. Hydrogen", "3. Oxygen", "4. Silicon"],
["1. Buses", "2. IT Sector", "3. Railways", "4. Banking Sector"],
["1. Limestone", "2. Black stone", "3. Red stone", "4. Grenite"],
["1. John delton", "2. Washington", "3. Polak", "4. Trumph"],
["1. By its octane number", "2. Iodine Value", "3. Cetaine Number", "4. Mass density"],
["1. Dengue", "2. Chinkengunia", "3. Rabies virus", "4. Cancer"],
["1. Prime Minister", "2. Deputy Minister", "3. President", "4. Chief Minister"],
["1. Extreme pressure ad heat","2. Extreme heat", "3. Extreme heat and pressure","4. Extreme pressure"],
["1. Mahatma Gandhi", "2. Jawahar Lal Nehru", "3. Ravindra Nath Tagore", "4. Bal Gangadhar Tilak"],
["1. largest railway station", "2. highest railway station", "3. longest railway station", "4. None of the above"],
["1. Insects", "2. Behavior of human beings", "3. The origin and history of technical and scientific terms", "4. The formation of rocks"],
["1. Asia", "2. Europe", "3. Africa", "4. Australia"],
["1. Junagarh, Gujarat", "2. Kohima, Nagaland", "3. Diphu, Assam", "4. Gangtok, Sikkim"],
["1. 7", "2. 9", "3. 8", "4. 10"]]

Audience_poll_list = [[56, 12, 18 , 14],[13, 8, 63, 16]]

answer_list = [1, 1, 3, 1, 3, 1, 3, 3, 3, 1, 1, 1, 3, 3, 3]

price_list = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 30000000, 50000000]

life_line_list = [ "5050", "Pass the question", "Audience poll", "power paplu"]
# power paplu is user can ask to use any lifline which is already used for 1 time.

pass_the_question = "What is the capital of punjab?"
pass_the_question_option = ["1. Chandigarh", "2. Ludhiyana", "3. Haryana", "4. Karnal"]
pass_the_question_answer = 1

p_pass_q = "Who is the lead actor in the movie Dilwale Dulhaniya le jaayenge? "
p_pass_o = ["1. Amitabh Bachhan", "2. Salman Khan", "3. Shahrukh khan", "4. Aamir Khan"]
p_pass_a = 3

lifeline_count = 0
lifeline_1 = 0
lifeline_2 = 0
lifeline_3 = 0
lifeline_4 = 0
i=0

# iterating loop on the question list
while i < len(Question_list):
	print ("\n", "This question is on your screens for price " + str(price_list[i]))
	print ("\n", Question_list[i])
	print ("\n", Option_list[i], "\n")
	if lifeline_count == 4:
		print (" You have used your all lifelines ", "\n")
	elif lifeline_count<4:
		lifeline = input(" 5050, Pass the question, Audience poll, Power Paplu:- choose any one lifeline " + "\n ")

	# 5050 lifeline
	if lifeline == "None":
		pass

	elif lifeline == "5050":
		if lifeline_1 == 0:
			Option_list[i].pop(1)
			Option_list[i].pop(2)
			print (Option_list[i], "\n")

			lifeline_count += 1
			lifeline_1 += 1
		else:
			print (" You have already used this lifeline! ","\n")

	# Pass the question lifline
	elif lifeline == "Pass the question":
		if lifeline_2 == 0:
			lifeline_count += 1
			lifeline_2 += 1
			i += 1
			print (pass_the_question,"\n")
			print (pass_the_question_option, "\n")
			user = int(input("enter your right anwer use only 1, 2, 3, 4 "+ "\n"))
			if user == pass_the_question_answer:
				print ("congratulations! You won " + str(price_list[i]) + " rupees!!", "\n")
				continue
			else:
				print ("you lose this game")
				break
		else:
			print ("You have already used this lifeline! ", "\n")


	# audience poll life line
	elif lifeline == "Audience poll":
		if lifeline_3 == 0:
			lifeline_3 +=1
			lifeline_count += 1
			if answer_list[i] == 1:
				print ("1. got " + str(Audience_poll_list[0][0]) +" %.", "\n")
				print ("2. got " + str(Audience_poll_list[0][1]) +" %.", "\n")
				print ("3. got " + str(Audience_poll_list[0][2]) +" %.", "\n")
				print ("4. got " + str(Audience_poll_list[0][3]) +" %.", "\n")
			elif answer_list[i] == 3:
				print ("1. got " + str(Audience_poll_list[1][0]) +" %.", "\n")
				print ("2. got " + str(Audience_poll_list[1][1]) +" %.", "\n")
				print ("3. got " + str(Audience_poll_list[1][2]) +" %.", "\n")
				print ("4. got " + str(Audience_poll_list[1][3]) +" %.", "\n")
		else:
			print ("You have already used this lifeline! ", "\n")
	# Power Paplu lifeline
	elif lifeline == "Power Paplu":
		if lifeline_4 == 0:
			lifeline_4 += 1
			lifeline_count +=1
			lifeline_p = input(" 5050, Pass the question, Audience poll :- choose any one lifeline ")
			if lifeline_p == "5050":
				Option_list[i].pop(1)
				Option_list[i].pop(2)
				print (Option_list[i])

			elif lifeline_p == "Audience poll":
				if answer_list[i] == 1:
					print ("1. got " + str(Audience_poll_list[0][0]) +" %.","\n")
					print ("2. got " + str(Audience_poll_list[0][1]) +" %.","\n")
					print ("3. got " + str(Audience_poll_list[0][2]) +" %.","\n")
					print ("4. got " + str(Audience_poll_list[0][3]) +" %.","\n")
				elif answer_list[i] == 3:
					print ("1. got " + str(Audience_poll_list[1][0]) +" %.","\n")
					print ("1. got " + str(Audience_poll_list[1][1]) +" %.","\n")
					print ("1. got " + str(Audience_poll_list[1][2]) +" %.","\n")
					print ("1. got " + str(Audience_poll_list[1][3]) +" %.","\n")
				
			elif lifeline_p == "Pass the question":
				print (p_pass_q)
				print (p_pass_o)
				user = int(input("enter your right anwer use only 1, 2, 3, 4 "))
				if user == p_pass_a:
					print ("congratulations! You won " + str(price_list[i]) + " rupees!!")
					i+=1
					continue
				else:
					print ("you lose this game")
					break
		else: 
			print ("You have already used this lifeline! ", "\n")


	user = int(input(" enter your right anwer use only 1, 2, 3, 4 "+ "\n "))
	if user == answer_list[i]:
		print ("congratulations! You won " + str(price_list[i]) + " rupees!!", "\n")
		i += 1
	else:
		print ("you lose this game")
		break
