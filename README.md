# KaRead
TTS for Kartvelian language (Georgian)

I am making Text To Speech for Kartvelian language. It will be a way different then most common tts that uses actual sounds from people. I choose Kartvelian becouse its my native language and also becouse pronunciation in Ka is way simpler than in most languages. Word is read letter by letter and letters are simple (maybe difficult for foreign but anyways...)

for example take Kartvelian word "ბავშვი"(bavshvi) means child in Ka... its read like:

b as in beer
a as in car
v as in vehicle
sh as in short
i as in list

and thats true for all words you'll see in Kartvelian.

I am getting letter frequencies with fourier transform from audacity.
after that I am separating them into vowels and consonants.
vowels are easier, just simple 4 or 5 sine waves multiplied by their db value and summed
consonants are kinda same but way shorter, usually a fraction of the milisecond, so kinda tricky to work with.

at this stage i made Pythone script that sums multiple frequencies and poop out array of values that after can be easier for another script to play, and theres our letter.

so far i can replicate any letter from sound
