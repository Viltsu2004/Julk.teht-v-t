const votes = []

const nCandidatesCount = Number(prompt("Monta vaali kandidaattia?"))


const setCandidatesData = (number) => {
  for (let i = 0; i < nCandidates; i++) {
    const name = prompt(`Name for it's "candidate" ${i + 1}:`)
    votes.push({name, votes: 0})
  }
}

function addVote(i) {
  if (votes[i]) {
    votes[i].votes += 100
  }
}

const nCandidates = nCandidatesCount
setCandidatesData(nCandidates)
addVote[i]

votes[1].votes += 100

votes.sort((a,b) => b.votes - a.votes)


const ul = document.querySelector("ul#root")

let k = 0;
while (k < votes.length) {
  const vote = votes[k]


  const li = document.createElement("li")

  li.innerText = `Nimi: ${vote.name} Votes: ${vote.votes}`

  ul.appendChild(li)
  k++
}

