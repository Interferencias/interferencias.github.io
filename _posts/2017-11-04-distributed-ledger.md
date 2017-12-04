---
layout: post
title: Distributed Ledger
author: terceranexus6
image:
  feature: banners/header.png
tags: security bitcoins distributed_ledger ledger blockchain
---

# Distributed Ledger and ethereum token creation

Basically, **distributed ledger** is the concept of sharing data evolution control in a common network. One of the most famous examples of this are BITCOINS, which works over a blockchain, a data base distributed between several participants (nodes) inside a ledger, which contains the updated status of each transaction between the nodes. These nodes are connected using a specific protocol.

The key of this system's movement lays on Token, elements that contains information and are encrypted. This token could act as a currency, vote, message, or anything that can be fixed in Distributed Ledger system. Several startups saw in this model new opportunities and efficient ways to approach to a better security and lower cost solutions. This way, DL is not always pictured in currency terms, but also thought to be an interesting option in energy industry ([Powerledger](https://tge.powerledger.io)), IoT ([Filament](https://filament.com)), communication or Voting systems ([Horizon State](https://horizonstate.com)).

**Beware!** Shitty diagram incoming:

![](https://github.com/terceranexus6/ethereum_lab/blob/master/images/diagram.jpg?raw=true)

Ethereum (an uprising cryptocurrency) has a wallet application that let developers freely deploy c++ contracts for token creation or nodes organizations in a virtual sandbox or in the real world. This is a lot of fun and makes the understanding of distributed ledger clearer for developers. The original documentation can be found [here](https://www.ethereum.org/dao) and [here](https://www.ethereum.org/token), and I will sum up how to create a token contract. Also, there's a wider explanation about DL in spanish and some contract examples in my [github repository](https://github.com/terceranexus6/ethereum_lab), please feel free to take a look at it and suggest any issues or PR. The project development is also pictured in a kanban styled board in the repo.

Okay so the basic token contract handles the initial supply of tokens that the owner (the contract developer) has, and the basic transfer funtion that includes checkings and token ownership changing.

```
contract MyToken {
    /* This creates an array with all balances */
    mapping (address => uint256) public balanceOf;

    /* Initializes contract with initial supply tokens to the creator of the contract */
    function MyToken(
        uint256 initialSupply
        ) {
        balanceOf[msg.sender] = initialSupply;              // Give the creator all initial tokens
    }

    /* Send coins */
    function transfer(address _to, uint256 _value) {
        require(balanceOf[msg.sender] >= _value);           // Check if the sender has enough
        require(balanceOf[_to] + _value >= balanceOf[_to]); // Check for overflows
        balanceOf[msg.sender] -= _value;                    // Subtract from the sender
        balanceOf[_to] += _value;                           // Add the same to the recipient
    }
}
```

But for creating a more complex cryptocurrency (that can be also used for other purposes such as voting, as mentioned) we should settle down some more details. For example, we should define the basic variables for the token identification:

```
// Public variables of the token
string public name;
string public symbol;
uint8 public decimals = 18;
// 18 decimals is the strongly suggested default, avoid changing it
```
And a more conplex transfer function which takes cares of saving balances for the future.

```
function _transfer(address _from, address _to, uint _value) internal {
    // Prevent transfer to 0x0 address. Use burn() instead
    require(_to != 0x0);
    // Check if the sender has enough
    require(balanceOf[_from] >= _value);
    // Check for overflows
    require(balanceOf[_to] + _value > balanceOf[_to]);
    // Save this for an assertion in the future
    uint previousBalances = balanceOf[_from] + balanceOf[_to];
    // Subtract from the sender
    balanceOf[_from] -= _value;
    // Add the same to the recipient
    balanceOf[_to] += _value;
    Transfer(_from, _to, _value);
    // Asserts are used to use static analysis to find bugs in your code. They should never fail
    assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
}
```
A function to destroy the tokens (the ones the participant owns) from the system (no take back!) or the ones from another participant.

```
function burn(uint256 _value) public returns (bool success) {
    require(balanceOf[msg.sender] >= _value);   // Check if the sender has enough
    balanceOf[msg.sender] -= _value;            // Subtract from the sender
    totalSupply -= _value;                      // Updates totalSupply
    Burn(msg.sender, _value);
    return true;
}

function burnFrom(address _from, uint256 _value) public returns (bool success) {
    require(balanceOf[_from] >= _value);                // Check if the targeted balance is enough
    require(_value <= allowance[_from][msg.sender]);    // Check allowance
    balanceOf[_from] -= _value;                         // Subtract from the targeted balance
    allowance[_from][msg.sender] -= _value;             // Subtract from the sender's allowance
    totalSupply -= _value;                              // Update totalSupply
    Burn(_from, _value);
    return true;
}
```
Also, a nice function would be the one who settles POW (proof of work) for getting the tokens and signing the transactions.


```
uint current = 1; // hehe try to guess the cubic root of the number. Imposible task >:)

    function rewardTheGenious(uint answer, uint next) {
        require(answer**3 == current); // goes on if it's correct
        balanceOf[msg.sender] += 1;         // reward the user!
        current = next;   // next test
    }
```
But unfortunately a computer finds this very easy, so maybe we should create a better Proof of work, that supposses a real challenge for a machine (those filthy smart toasters!):

```
    bytes32 public currentChallenge;                         // The coin starts with a challenge
    uint public timeOfLastProof;                             // Variable to keep track of when rewards were given
    uint public difficulty = 10**32;                         // Difficulty starts reasonably low

    function proofOfWork(uint nonce){
        bytes8 n = bytes8(sha3(nonce, currentChallenge));    // Generate a random hash based on input
        require(n >= bytes8(difficulty));                   // Check if it's under the difficulty

        uint timeSinceLastProof = (now - timeOfLastProof);  // Calculate time since last reward was given
        require(timeSinceLastProof >=  5 seconds);         // Rewards cannot be given too quickly
        balanceOf[msg.sender] += timeSinceLastProof / 60 seconds;  // The reward to the winner grows by the minute

        difficulty = difficulty * 10 minutes / timeSinceLastProof + 1;  // Adjusts the difficulty

        timeOfLastProof = now;                              // Reset the counter
        currentChallenge = sha3(nonce, currentChallenge, block.blockhash(block.number - 1));  // Save a hash that will be used as the next proof
    }
```

Once our token looks just like we wanted we can deploy it using the ethereum wallet sandbox. The interface is quite simple, only add the code in the editor box, fill the options you coded (name or symbol, for example, good news you can use emoticons!) and click in Deploy. For this only set the **correct Network** (virtual sandbox, there are a couple), click on **contracts** and look for the "**DEPLOY NEW CONTRACT**" button.

![](https://www.ethereum.org/images/tutorial/deploy-new-contract.png)
![](https://www.ethereum.org/images/tutorial/edit-contract.png)

Anyway I think as a research experiment to better understand the criptocurrencies is pretty neat. I aim to write a refined token contract on my own as well as a contract to organize several nodes in the blockchain. Hope you guys found it as fun as I did!
