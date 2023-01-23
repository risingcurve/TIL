## GIT

* `git init` : 깃으로 관리하기
* `git status` : 파일 관리 현황
* `git add .` : 지금 다 올려!

  * `git add <file_name.ext> <file_name.ext>`
* `git commit -m '<commit_message>'`
* `git push origin master`
* `git pull origin master`
* 계정 연결

  * `git config --local user.name '<username>'`
  * `git config --local user.email '<email>'`
* 레포 연결

  * `git remote add origin <레포 주소>`
* Undoing (돌아가기)
  1. Working Directory 작업 단계 
    * `git restore {file_name.ext}
  
  2. Staging Area 작업 단계 
    * root-commit이 없는 경우
      * `git rm --cached {file_name.ext}
    * root-commit이 있는 경우
      * `git restore --staged {file_name.ext}

  3. Repository 작업 단계 
    * `git commit --amend` 

* reset (돌아가기)
  * `git reset [옵션] {커밋번호}`
  * --soft (staging area로 돌아가기)
  * --mixed (working directory로 돌아가기)
  * --hard (완전삭제)

* revert (돌아가기)
  * `git revert {커밋번호}`
  * {커밋번호}의 내용은 없던 일이 되고 **새로운 커밋**이 생성됨
    * `git log --oneline`으로 확인!

reset - > 커밋 내역 삭제
revert -> 커밋을 새로 쌓는다

* Branch (브랜치)

  * `git branch` : 로컬 저장소(git) 브랜치 목록 확인
  * `git branch -r` : 원격 저장소(github) 의 브랜치 목록 확인

  * `git branch {브랜치 이름}` : 브랜치 생성
    * 이미 있는 브랜치 이름 안됨! 새로운 이름 작성 필수!
  * `git branch {브랜치 이름} {커밋 ID} # 특정 기준으로 브랜치 생성

  * `git  branch -d {브랜치 이름}` : merge를 해야지만 삭제할 수 있는 권한이 생김
  * `git branch -D {브랜치 이름}`: 강제 삭제 
    * merge -> 귀찮아서보다는... 완전 삭제하고 싶어서 사용하는 편

  * `git checkout {브랜치 이름}`: 다른 브랜치로 이동
  * `git switch {브랜치 이름}` : 다른 브랜치로 이동

  * `git switch -c {브랜치 이름}` : 브랜치를 새로 생성하고 바로 이동
  * `git switch -c {브랜치 이름} {커밋 ID}`: 특정 커밋 기준으로 브랜치 생성 및 이동
  
  * 브랜치 변경 전에 반드시!! COMMIT 해야지만 브랜치를 이동할 수 있따. 

* merge (병합)
  * `git merge {합칠 브랜치 이름}`
  1. Fast Forward
  2. 3 way Merge
  3. Merge Conflict




