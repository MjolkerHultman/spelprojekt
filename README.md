'''


Maybe an interactive shop thang? Could make a shopkeep with dialogue incorporating polymorphism for the purposes of demonstration. Selling point information about each item on sale?

Gameplay would boil down to buying things. Maybe flipping stuff for a profit? Simple enough. Probably. Not if i look at it for too long. The prospect of a bartering system scares me.

How would that even work? Random number between the true value of the item and an acceptable maximum/minimum decides their absolute limits, if the player suggests a deal above/below those limits respectively they immediately cancel the transaction, anything between there is fine. Random chance entirely. Maybe have an additional value denoting their preffered/"happy-to-pay" price, decided after their max/min values have been taken into account?

^this is very uninteractive. Bartering loop where you try to guess is undebatably the easiest method, but as for what to do with that afterwards is another question.

maybe allow a bartering attempt from the opponent with a random(?) multiplier?

First things first, there must be at least two "opponents", one of which sells, one of which buys. Flavour is probably the easiest thing to chuck in, though I suppose it might take some time to write the dialogue. Not that bad, probably. Nevermind. What're we selling? RPG store with whatever neat little trinkets and a rusty short-sword or two? Sounds fun to write.

Magical orb that's always 30 degrees is a fun one. A sock that's twice as big on the inside as it appears, shrinking people's feet sounds funny. A flying matchbox that eats fireflies, a metal pipe that flexes as though it were made of rope yet remains watertight, A seemingly normal walking stick that gives you great luck when it comes to trecking around, still salty about that bloody ditch, and whatever else fun kind of goober-ass kind of magical items I might think of along the way.

Shopkeepers as a class, with a "stingy" multiplier of how wide their range of acceptable prices is, and then maybe a favourite ware or something?


Aight, how do I go about actually structuring the bartering loop?
Whilst both parties haven't fucked up too bad, which is defined later, run the loop.

Roll "initiative", random int multiplied by the ratio between purse values to determine who gets to make the first offer


'''