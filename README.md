MeemLev Docs
=======================================================
## Table of Contents

 * [Overview](#overview)
 * [Demo](#demo)
 * [DAO Presets](#dao-presets)
 * [MeemLev Public API](#meemlev-public-api)


# Overview
Welcome to MeemLev General repo.
This repository hosts general docs for MeemLev. You can find the following:
- MeemLev [Whitepaper](https://github.com/meemlev/general/blob/main/MeemLev_wp.pdf)
- Documentation for MeemLev Public API to interact with MeemLev contract on the blockchain.
- MeemLev DAO proposals are handled through this repo as well

# Demo
Video below shows how to interact with the MeemLev Contract on the Sepolia Network through MeemHub.

https://github.com/meemlev/general/assets/166253179/8d6ca66b-75cd-4fae-8a0b-0ea930a71e8f

---
# DAO Presets

### General configurations
```yaml
_maxActiveProposals: 3
_minVoterStake: 1000
_minProposerStake: 100000
_minStakingDuration: 7 days
_stakingBaseDuration: 14 days
_durationCapFactor: 10
```

### Categories configurations
```yaml
// Rewards
maxVotingDuration: 14 days
minVotingDuration: 7 days
quorum: 90%

// Ecosystem
maxVotingDuration: 14 days
minVotingDuration: 7 days
quorum: 90%

// Founders
maxVotingDuration: 7 days
minVotingDuration: 3 days
quorum: 90%

// Team
maxVotingDuration: 7 days
minVotingDuration: 3 days
quorum: 90%
```

---
# MeemLev Public API
The upcoming MeemLev Public API will offer users and developers a user-friendly REST API for seamless interaction with the MeemLev contract. Stay tuned as we prepare to roll out this API soon. Below, you'll find the preliminary definition of the API set to be released

## Public Callables

### Welcome Message

- **URL:** `/`
- **Method:** `GET`
- **Description:** Displays a welcome message with a link to the API documentation.

---

### Decimals

- **URL:** `/decimals`
- **Method:** `GET`
- **Description:** Retrieves the number of decimal places for the token.
- **Response**:
  - 200 OK: JSON object with the number of decimals.

---

### Deploy Timestamp

- **URL:** `/deployTimestamp`
- **Method:** `GET`
- **Description:** Retrieves the timestamp when the contract was deployed.
- **Response**:
  - 200 OK: JSON object with the timestamp.

---

### Name

- **URL:** `/name`
- **Method:** `GET`
- **Description:** Retrieves the name of the token.
- **Response**:
  - 200 OK: JSON object with the name of the token.

---

### Owner

- **URL:** `/owner`
- **Method:** `GET`
- **Description:** Retrieves the owner address of the contract.
- **Response**:
  - 200 OK: JSON object with the owner address of the contract.

---

### Symbol

- **URL:** `/symbol`
- **Method:** `GET`
- **Description:** Retrieves the symbol of the token.
- **Response**:
  - 200 OK: JSON object with the symbol of the token.

---

### Allowance

- **URL:** `/allowance`
- **Method:** `GET`
- **Description:** Retrieves the allowance granted by the owner to the spender.
- **Query Parameters:**
  - `owner`: The address of the owner.
  - `spender`: The address of the spender.
- **Response**:
  - 200 OK: JSON object with the allowance granted by the owner to the spender.

---

### Total Supply

- **URL:** `/totalSupply`
- **Method:** `GET`
- **Description:** Retrieves the total supply of the token.
- **Response**:
  - 200 OK: JSON object with the total supply of the token.

---

### Balance Of

- **URL:** `/balanceOf`
- **Method:** `GET`
- **Description:** Retrieves the balance of the specified account.
- **Query Parameters:**
  - `account`: The address of the account.
- **Response**:
  - 200 OK: JSON object with the balance of the specified account.

---

### Burnt Tokens

- **URL:** `/burntTokens`
- **Method:** `GET`
- **Description:** Retrieves the total number of burnt tokens.
- **Response**:
  - 200 OK: JSON object with the total number of burnt tokens.

---

### Circulating Supply

- **URL:** `/circulatingSupply`
- **Method:** `GET`
- **Description:** Retrieves the circulating supply of the token.
- **Response**:
  - 200 OK: JSON object with the circulating supply of the token.

## MeemLev Callables

### ZFC Config

- **URL:** `/zfc_config`
- **Method:** `GET`
- **Description:** Retrieves configuration information for ZFC.
- **Response**:
  - 200 OK: JSON object with ZFC configuration information.

---

### ZRC Config

- **URL:** `/zrc_config`
- **Method:** `GET`
- **Description:** Retrieves configuration information for ZRC.
- **Response**:
  - 200 OK: JSON object with ZRC configuration information.

---

### ZGC Category Config

- **URL:** `/zgc_categoryConfig`
- **Method:** `GET`
- **Description:** Retrieves configuration information about a specific category.
- **Query Parameters:**
  - `category`: The category ID (optional).
- **Response**:
  - 200 OK: JSON object with the category configuration information.

---

### ZGC DAO Config

- **URL:** `/zgc_DAOconfig`
- **Method:** `GET`
- **Description:** Retrieves configuration information for the ZGC DAO.
- **Response**:
  - 200 OK: JSON object with the ZGC DAO configuration information.

---

### ZTC Vesting Grants

- **URL:** `/ztc_vestingGrants`
- **Method:** `GET`
- **Description:** Retrieves information about ZTC vesting grants.
- **Response**:
  - 200 OK: JSON object with ZTC vesting grants information.

---

### ZRC Scheduled Reward Times

- **URL:** `/zrc_scheduledRewardTimes`
- **Method:** `GET`
- **Description:** Retrieves scheduled reward times for ZRC.
- **Response**:
  - 200 OK: JSON object with ZRC scheduled reward times.

---

### ZGC Existing Proposals

- **URL:** `/zgc_existingProposals`
- **Method:** `GET`
- **Description:** Retrieves information about existing proposals in ZGC.
- **Response**:
  - 200 OK: JSON object with existing proposals information.

---

### ZGC Get Proposal Parameters

- **URL:** `/zgc_getProposalParameters`
- **Method:** `GET`
- **Description:** Retrieves parameters of a specific proposal from the Governance contract.
- **Query Parameters:**
  - `proposal_id`: The ID of the proposal to retrieve parameters for.
- **Response**:
  - 200 OK: JSON object with the parameters of the specified proposal.

---

### ZGC Proposals

- **URL:** `/zgc_proposals`
- **Method:** `GET`
- **Description:** Retrieves information about proposals in ZGC.
- **Query Parameters:**
  - `proposal_id`: The ID of the proposal to retrieve information for (optional).
- **Response**:
  - 200 OK: JSON object with proposals information.

## Public Transactables

### Decrease Allowance

- **URL:** `/decreaseAllowance`
- **Method:** `POST`
- **Description:** Decreases the allowance granted by the owner to the spender.
- **Request Body:**
  - `spender`: The address of the spender.
  - `subtracted_value`: The amount by which the allowance will be decreased.
- **Response**:
  - 200 OK: JSON object with the transaction ID.

---

### Increase Allowance

- **URL:** `/increaseAllowance`
- **Method:** `POST`
- **Description:** Increases the allowance granted by the owner to the spender.
- **Request Body:**
  - `spender`: The address of the spender.
  - `added_value`: The amount by which the allowance will be increased.
- **Response**:
  - 200 OK: JSON object with the transaction ID.

---

### Transfer

- **URL:** `/transfer`
- **Method:** `POST`
- **Description:** Transfers tokens to a specified recipient.
- **Request Body:**
  - `recipient`: The address of the recipient.
  - `amount`: The amount of tokens to transfer.
- **Response**:
  - 200 OK: JSON object with the transaction ID.

---

### Approve

- **URL:** `/approve`
- **Method:** `POST`
- **Description:** Approves the spender to spend a specified amount of tokens on behalf of the owner.
- **Request Body:**
  - `spender`: The address of the spender.
  - `amount`: The amount of tokens to approve.
- **Response**:
  - 200 OK: JSON object with the transaction ID.

---

### Transfer From

- **URL:** `/transferFrom`
- **Method:** `POST`
- **Description:** Transfers tokens from one address to another on behalf of a specified address.
- **Request Body:**
  - `sender`: The address from which the tokens are transferred.
  - `recipient`: The address to which the tokens are transferred.
  - `amount`: The amount of tokens to transfer.
- **Response**:
  - 200 OK: JSON object with the transaction ID.

## MeemLev Transactables

### ZTC Claim Grant

- **URL:** `/ztc_claimGrant`
- **Method:** `POST`
- **Description:** Claims the grant for a member.
- **Response:**
  - 200 OK: JSON object with the transaction ID.

---

### ZGC DAO Stake

- **URL:** `/zgc_DAOstake`
- **Method:** `POST`
- **Description:** Retrieves stake information for a DAO member.
- **Request Body:**
  - `member_address` (str): The address of the DAO member.
- **Response:**
  - 200 OK: JSON object with the following stake information:
    - `timestamp` (int): The timestamp of the stake.
    - `balance` (int): The balance of the stake.

---

### ZGC Vote

- **URL:** `/zgc_vote`
- **Method:** `POST`
- **Description:** Votes for a proposal.
- **Request Body:**
  - `proposal_id` (int): The ID of the proposal to vote for.
  - `support` (int): The support value for the vote.
- **Response:**
  - 200 OK: JSON object with the transaction ID.

---

### ZGC Stake DAO Tokens

- **URL:** `/zgc_stakeDAOTokens`
- **Method:** `POST`
- **Description:** Stakes DAO tokens.
- **Request Body:**
  - `amount` (int): The amount of tokens to stake.
- **Response:**
  - 200 OK: JSON object with the transaction ID.

---

### ZGC Unstake DAO Tokens

- **URL:** `/zgc_unstakeDAOTokens`
- **Method:** `POST`
- **Description:** Unstakes DAO tokens.
- **Request Body:**
  - `amount` (int): The amount of tokens to unstake.
- **Response:**
  - 200 OK: JSON object with the transaction ID.


