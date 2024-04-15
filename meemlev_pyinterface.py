from abc import ABC, abstractmethod
from typing import Dict, List, Any


class PublicCallablestInterface(ABC):
    """
    Abstract base class defining interface for interacting with a token smart contract.
    """

    @abstractmethod
    def decimals(self) -> int:
        """
        Retrieve the number of decimal places for the token.
        """
        pass

    @abstractmethod
    def allowance(self, owner: str, spender: str) -> int:
        """
        Retrieves the allowance granted by the owner to the spender.
        """
        pass

    @abstractmethod
    def totalSupply(self) -> int:
        """
        Retrieve the total supply of the token.
        """
        pass

    @abstractmethod
    def balanceOf(self, account: str) -> int:
        """
        Retrieves the balance of the specified account.
        """
        pass

    @abstractmethod
    def burntTokens(self) -> int:
        """
        Retrieve the total number of burnt tokens.
        """
        pass

    @abstractmethod
    def circulatingSupply(self) -> int:
        """
        Retrieve the circulating supply of the token.
        """
        pass

    @abstractmethod
    def deployTimestamp(self) -> int:
        """
        Get the timestamp when the contract was deployed.
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """
        Retrieve the name of the token.
        """
        pass

    @abstractmethod
    def owner(self) -> str:
        """
        Retrieve the owner address of the contract.
        """
        pass

    @abstractmethod
    def symbol(self) -> str:
        """
        Retrieve the symbol of the token.
        """
        pass

class PublicTransactablesInterface(ABC):
    """
    Abstract class defining an interface for interacting with token smart contracts.
    """

    @abstractmethod
    def burn(self, amount: int) -> str:
        """
        Burns a specified amount of tokens.

        Parameters:
        - amount (int): The amount of tokens to burn.
        
        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def transfer(self, recipient: str, amount: int) -> str:
        """
        Transfers tokens to a specified address.

        Parameters:
        - recipient (str): The address to transfer tokens to.
        - amount (int): The amount of tokens to transfer.

        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def approve(self, spender: str, amount: int) -> str:
        """
        Approves a spender to spend a specified amount of tokens on behalf of the owner.

        Parameters:
        - spender (str): The address of the spender.
        - amount (int): The amount of tokens to approve.

        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def transferFrom(self, sender: str, recipient: str, amount: int) -> str:
        """
        Transfers tokens from one account to another.

        Parameters:
        - sender (str): The address of the sender.
        - recipient (str): The address of the recipient.
        - amount (int): The amount of tokens to transfer.

        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def decreaseAllowance(self, spender: str, subtracted_value: int) -> str:
        """
        Decreases the allowance of a spender.

        Parameters:
        - spender (str): The address of the spender.
        - subtracted_value (int): The amount by which to decrease the allowance.

        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def increaseAllowance(self, spender: str, added_value: int) -> str:
        """
        Increases the allowance of a spender.

        Parameters:
        - spender (str): The address of the spender.
        - added_value (int): The amount by which to increase the allowance.

        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def renounceOwnership(self) -> str:
        """
        Renounces ownership of the contract.
        
        Returns:
        - str: Transaction ID
        """
        pass

    @abstractmethod
    def transferOwnership(self, new_owner: str) -> str:
        """
        Transfers ownership of the contract to a new owner.

        Parameters:
        - new_owner (str): The address of the new owner.
        
        Returns:
        - str: Transaction ID
        """
        pass

class MeemLevCallablesInterface(ABC):
    @abstractmethod
    def zfc_config(self) -> Dict[str, Any]:
        """Retrieve configuration information about the ZFC token."""
        pass

    @abstractmethod
    def ztc_vestingGrants(self) -> int:
        """Retrieve the vesting grants."""
        pass

    @abstractmethod
    def ztc_getMember(self, member_address: str, secret: str) -> Dict[str, int]:
        """Retrieve information about a member."""
        pass

    @abstractmethod
    def zrc_config(self) -> Dict[str, int]:
        """Retrieve configuration information about the ZRC token."""
        pass

    @abstractmethod
    def zrc_scheduledRewardTimes(self) -> List[int]:
        """Retrieve scheduled reward times information from the ZRC token."""
        pass

    @abstractmethod
    def zgc_categoryConfig(self, category: int=None) -> Dict[str, Any]:
        """Retrieve configuration information about a specific category."""
        pass

    @abstractmethod
    def zgc_DAOconfig(self) -> Dict[str, int]:
        """Retrieve configuration information about the DAO."""
        pass

    @abstractmethod
    def zgc_existingProposals(self) -> List[int]:
        """Retrieve existing proposals from the Governance contract."""
        pass

    @abstractmethod
    def zgc_getProposalParameters(self, proposal_id: int) -> List[int]:
        """Retrieve parameters of a specific proposal from the Governance contract."""
        pass

    @abstractmethod
    def zgc_proposals(self, proposal_id: int=None) -> Dict[str, Any]:
        """Retrieve information about a proposal."""
        pass

    @abstractmethod
    def zgc_DAOstake(self, member_address: str) -> Dict[str, int]:
        """Retrieve stake information for a DAO member."""
        pass

class MeemLevTransactablesInterface(ABC):
    @abstractmethod
    def initializeContract(self, founders: str, team: str, rewards: str, ecosystem: str, stake: str) -> str:
        """Initializes the contract with specified addresses."""
        pass

    @abstractmethod
    def zfc_claimGrant(self, to_address: str) -> str:
        """Claims a grant for the specified address."""
        pass

    @abstractmethod
    def zfc_updateConfig(self, proposal_id: int) -> str:
        """Updates the configuration."""
        pass

    @abstractmethod
    def ztc_addMember(self, member_address: str, grant: int, round_target: int, frequency: int) -> Dict[str, str]:
        """Adds a new member to the contract."""
        pass

    @abstractmethod
    def ztc_deleteMember(self, member_address: str) -> str:
        """Deletes a member from the contract."""
        pass

    @abstractmethod
    def ztc_updateMember(self, member_address: str, grant: int, round_target: int, frequency: int) -> str:
        """Updates the details of a member in the contract."""
        pass

    @abstractmethod
    def ztc_claimGrant(self) -> str:
        """Claims the grant for a member."""
        pass

    @abstractmethod
    def zrc_setAnnualBudget(self) -> str:
        """Sets the annual budget for the current year."""
        pass

    @abstractmethod
    def zrc_unlockRewards(self) -> str:
        """Unlocks rewards for the upcoming round."""
        pass

    @abstractmethod
    def zrc_distributeRewards(self, to_address: str, amount: int) -> str:
        """Distributes rewards to a specified address."""
        pass

    @abstractmethod
    def zrc_updateConfig(self, proposal_id: int) -> str:
        """Updates the configuration based on the proposal ID."""
        pass

    @abstractmethod
    def zec_transferFunds(self, proposal_id: int, to_address: str) -> str:
        """Transfers funds to a specified address."""
        pass

    @abstractmethod
    def zgc_createProposal(self, description: str, voting_duration: int, category: int, parameters: List[int]) -> str:
        """Creates a new proposal."""
        pass

    @abstractmethod
    def zgc_vote(self, proposal_id: int, support: int) -> str:
        """Votes for a proposal."""
        pass

    @abstractmethod
    def zgc_deleteProposal(self, proposal_id: int) -> str:
        """Deletes a proposal."""
        pass

    @abstractmethod
    def zgc_executeProposal(self, proposal_id: int, category: int) -> List[int]:
        """Executes a proposal."""
        pass

    @abstractmethod
    def zgc_setCategoryConfig(self, category: int, max_voting_duration: int, min_voting_duration: int, quorum: int) -> str:
        """Sets the configuration for a specific proposal category."""
        pass

    @abstractmethod
    def zgc_setDAOConfig(self, max_active_proposals: int, min_voter_stake: int, min_proposer_stake: int,
                           min_staking_duration: int, staking_base_duration: int, duration_cap_factor: int) -> str:
        """Sets the configuration for DAO operations."""
        pass

    @abstractmethod
    def zgc_stakeDAOTokens(self, amount: int) -> str:
        """Stakes DAO tokens."""
        pass

    @abstractmethod
    def zgc_unstakeDAOTokens(self, amount: int) -> str:
        """Unstakes DAO tokens."""
        pass

class MeemLevInterface(PublicCallablestInterface, PublicTransactablesInterface,
                       MeemLevCallablesInterface, MeemLevTransactablesInterface):
    pass