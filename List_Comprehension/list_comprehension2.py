# https://www.youtube.com/watch?v=AhSvKGTh28Q&ab_channel=Socratica

squares = []
for i in range(1,101):
    squares.append(i**2)
print("square",squares)

squares2 = [i**2 for i in range(1,101)]
print("squares2",squares2)


###########################################################################################
titles = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toyory", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard o if Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Wi11 Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day",
"Close Encounters of the Third Kind"]


movies = [title  for title in titles  if title.startswith("G")]
print("movies with G ", movies)