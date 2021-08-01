{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "from github import Github\n",
    "import random\n",
    "\n",
    "repository = \"jiangxyz/test_githublottery\"\n",
    "github_username = \"jiangxyz\"\n",
    "github_password = \"\"\n",
    "N = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_lucky_dogs():\n",
    "    # First create a Github instance\n",
    "    # g = Github()\n",
    "    # Or you can use your GitHub username and password\n",
    "    g = Github(github_username, github_password)\n",
    "\n",
    "    # Get a repo by repo-name\n",
    "    repo = g.get_repo(repository)\n",
    "\n",
    "    # Now list the users\n",
    "    stared_users = []\n",
    "    for user in repo.get_stargazers():\n",
    "        stared_users.append(user)\n",
    "    # 返回所有star用户的username的列表\n",
    "    return stared_users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running...\n",
      "Found [NamedUser(login=\"jiangxyz\")] \n",
      "1 stared users in total.\n",
      "\n",
      "\n",
      "--- Congratulations!!! --- \n",
      "\n",
      "\n",
      "jiangxyz (None)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"Running...\")\n",
    "    stared_users = get_lucky_dogs()\n",
    "    print(\"Found {} \".format(stared_users))\n",
    "    print(\"{} stared users in total.\".format(len(stared_users)))\n",
    "\n",
    "    print(\"\\n\\n--- Congratulations!!! --- \\n\\n\")\n",
    "    alist = random.sample(range(0, len(stared_users)), N) # sample 用于无重复的随机抽样\n",
    "    [print(\"{} ({})\".format(stared_users[i].login, stared_users[i].email)) for i in alist]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
