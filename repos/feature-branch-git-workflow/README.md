# feature-branch-git-workflow
Introduces the git feature branch workflow recommended for DSI case studies.


## DSI Case Studies  
Case studies in the DSI serve multiple purposes: review and solidify technologies
introduced earlier in the week, develop code unconstrained by assignment 
objectives, provide experience scoping and executing a project in a short period
of time, practice collaborating on git, and finally (and most importantly) 
development of your soft-skills: those behaviors that enable someone to interact
effectively and harmoniously with other people.

With that in mind, what makes a good team?

## What Google Learned from its Quest to Build the Perfect Team  
In [2016 the NYT published an article](https://www.nytimes.com/2016/02/28/magazine/what-google-learned-from-its-quest-to-build-the-perfect-team.html) on Google's multi-year study on what led
to effective teams in the tech space.  There were several highlights.

**Who didn't seem to matter**  
> We had lots of data, but there was nothing showing that a mix of specific
  personality types or skills or backgrounds made any difference.  The "who"
  part of the equation didn't seem to matter.

what did matter:  
**Collective intelligence**  
> As long as everyone got a chance to talk, the team did well.  But if only
  one person or a small group spoke all the time, the collective intelligence
  declined.

Please keep this in mind.  You all are working together for the next 3 months.  
Fostering strong relationships, listening to and learning from your classmates 
should be just as important as "getting the job done."  

## Collaborating on Git  
There are multiple ways, called workflows, to work as a group on a coding project.  The [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
is recommended for DSI case studies.  The Feature Branch Workflow:  
* Assumes a central repository, where one of the group case study members forks
  the Galvanize case study repository and then all other group members `clone` that
  person's repository. (Everyone's `origin` is the same remote).
* Utilizes [branches](https://www.atlassian.com/git/tutorials/using-branches)
  to separate working & sharable code on the `master` branch with code being
  developed in development branches.  As the project proceeds, code in the 
  development branches is merged into the `master`, and pulled by all case study
  members to work with.
* Assumes that whatever in the `master` branch is deployed code.  You **NEVER** 
  work on the `master` branch.  You work on development branches (we recommend
  using your name as the branch name) and then those branches get merged
  into the master branch.
* In case studies, as code is developed it gets merged into the `master` branch
  and people pull it to get access to it.  Then they promptly branch off `master`
  to do more development work.

Branches in git are simply pointers to commits.  When you make a new branch, you're
making a new pointer to a commit.  You can have multiple pointers for a given commit,
and git keeps track of what pointer you are using by giving it a special name, HEAD.
Please refer to figures 3-1 to 3-7 [here](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

## Practice  
Get in to your case study groups, have one person fork this repo from Galvanize,
and have everyone else clone that repo.  Then do the two exercises in [assignment.md.](https://github.com/GalvanizeDataScience/feature-branch-git-workflow/blob/master/assignment.md)



