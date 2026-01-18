Branch Strategy :
	Branch for every new feature, all development happens in feature branches, all f	ixes will happen in hotfix branches

Commit Message : 
	Use prefix for clarity on which problem you are addressing. Like feat for featur	e and fix for hot fixes.
	EX : 
		Feat : added addtion operator
		Hotfix : fixed grammar mistakes

Code Review Process :
	First : make a pull request for feature branch
	Second : make a dedicated review group
	Third : check for functionality, proper coding conventions, and useful comments
	Fourth : merge after successful review and tests

Release Workflow :
	First : merge all feature branches together into the main branch 
	Second : Resolve any errors if there are any
	Third : label the release with version (v1.0)
	Fourth : update the README file accordingly with changes or additions

Git commands : 
	Clone : git clone <https>
	Create Branch : git branch <name>
	Check Branch : git branch
	Switch Branch : git switch <name>
	Add file : git add <file/.>
	Commit Change : git commit -m "<document changes>"
	Push changes : git push origin <branch>
	Pull changes : git pull origin <branch>
	Merge branch : git merge <branch>
	Check status : git status	
