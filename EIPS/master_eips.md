#eip-1.md
    EIP: 1
      Title: EIP Purpose and Guidelines
      Status: Draft
      Type: Meta
      Author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>
      Created: 2015-10-27, 2017-02-01

What is an EIP?
--------------

EIP stands for Ethereum Improvement Proposal. An EIP is a design document providing information to the Ethereum community, or describing a new feature for Ethereum or its processes or environment. The EIP should provide a concise technical specification of the feature and a rationale for the feature. The EIP author is responsible for building consensus within the community and documenting dissenting opinions.

EIP Rational
------------

We intend EIPs to be the primary mechanisms for proposing new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Ethereum. Because the EIPs are maintained as text files in a versioned repository, their revision history is the historical record of the feature proposal.

For Ethereum implementers, EIPs are a convenient way to track the progress of their implementation. Ideally each implementation maintainer would list the EIPs that they have implemented. This will give end users a convenient way to know the current status of a given implementation or library.

EIP Types
---------

There are three types of EIP:

-   A **Standard Track EIP** describes any change that affects most or all Ethereum implementations, such as a change to the the network protocol, a change in block or transaction validity rules, proposed application standards/conventions, or any change or addition that affects the interoperability of applications using Ethereum. Furthermore Standard EIPs can be broken down into the following categories.
    -   **Core** - improvements requiring a consensus fork (e.g. [EIP5], [EIP101]), as well as changes that are not necessarily consensus critical but may be relevant to “core dev” discussions (for example, [EIP90], and the miner/node strategy changes 2, 3, and 4 of [EIP86]).
    -   **Networking** - includes improvements around [devp2p] ([EIP8]) and [Light Ethereum Subprotocol], as well as proposed improvements to network protocol specifications of [whisper] and [swarm].
    -   **Interface** - includes improvements around client [API/RPC] specifications and standards, and also certain language-level standards like method names ([EIP59], [EIP6]) and [contract ABIs]. The label “interface” aligns with the [interfaces repo] and discussion should primarily occur in that repository before an EIP is submitted to the EIPs repository.
    -   **ERC** - application-level standards and conventions, including contract standards such as token standards ([ERC20]), name registries ([ERC26], [ERC137]), URI schemes ([ERC67]), library/package formats ([EIP82]), and wallet formats ([EIP75], [EIP85]).

-   An **Informational EIP** describes a Ethereum design issue, or provides general guidelines or information to the Ethereum community, but does not propose a new feature. Informational EIPs do not necessarily represent Ethereum community consensus or a recommendation, so users and implementers are free to ignore Informational EIPs or follow their advice.
-   A **Meta EIP** describes a process surrounding Ethereum or proposes a change to (or an event in) a process. Process EIPs are like Standards Track EIPs but apply to areas other than the Ethereum protocol itself. They may propose an implementation, but not to Ethereum's codebase; they often require community consensus; unlike Informational EIPs, they are more than recommendations, and users are typically not free to ignore them. Examples include procedures, guidelines, changes to the decision-making process, and changes to the tools or environment used in Ethereum development. Any meta-EIP is also considered a Process EIP.

EIP Work Flow
-------------

The EIP repository Collaborators change the EIPs status. Please send all EIP-related email to the EIP Collaborators, which is listed under EIP Editors below. Also see EIP Editor Responsibilities & Workflow.

The EIP process begins with a new idea for Ethereum. It is highly recommended that a single EIP contain a single key proposal or new idea. The more focused the EIP, the more successful it tends to be. A change to one client doesn't require an EIP; a change that affects multiple clients, or defines a standard for multiple apps to use, does. The EIP editor reserves the right to reject EIP proposals if they appear too unfocused or too broad. If in doubt, split your EIP into several well-focused ones.

Each EIP must have a champion - someone who writes the EIP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea.

Vetting an idea publicly before going as far as writing an EIP is meant to save the potential author time. Asking the Ethereum community first if an idea is original helps prevent too much time being spent on something that is guaranteed to be rejected based on prior discussions (searching the Internet does not always do the trick). It also helps to make sure the idea is applicable to the entire community and not just the author. Just because an idea sounds good to the author does not mean it will work for most people in most areas where Ethereum is used. Examples of appropriate public forums to gauge interest around your EIP include [the Ethereum subreddit], [the Issues section of this repository], and [one of the Ethereum Gitter chat rooms]. In particular, [the Issues section of this repository] is an excellent place to discuss your proposal with the community and start creating more formalized language around your EIP. 

Once the champion has asked the Ethereum community whether an idea has any chance of acceptance a draft EIP should be presented as a [pull request]. This gives the author a chance to continuously edit the draft EIP for proper formatting and quality. This also allows for further public comment and the author of the EIP to address concerns about the proposal.

If the EIP collaborators approve, the EIP editor will assign the EIP a number (generally the issue or PR number related to the EIP), label it as Standards Track, Informational, or Meta, give it status “Draft”, and add it to the git repository. The EIP editor will not unreasonably deny an EIP. Reasons for denying EIP status include duplication of effort, being technically unsound, not providing proper motivation or addressing backwards compatibility, or not in keeping with the Ethereum philosophy.

Standards Track EIPs consist of three parts, a design document, implementation, and finally if warranted an update to the [formal specification]. The EIP should be reviewed and accepted before an implementation is begun, unless an implementation will aid people in studying the EIP. Standards Track EIPs must be implemented in at least three viable Ethereum clients before it can be considered Final.

For an EIP to be accepted it must meet certain minimum criteria. It must be a clear and complete description of the proposed enhancement. The enhancement must represent a net improvement. The proposed implementation, if applicable, must be solid and must not complicate the protocol unduly.

Once an EIP has been accepted, the implementations must be completed. When the implementation is complete and accepted by the community, the status will be changed to “Final”.

An EIP can also be assigned status “Deferred”. The EIP author or editor can assign the EIP this status when no progress is being made on the EIP. Once an EIP is deferred, the EIP editor can re-assign it to draft status.

An EIP can also be “Rejected”. Perhaps after all is said and done it was not a good idea. It is still important to have a record of this fact.

EIPs can also be superseded by a different EIP, rendering the original obsolete.

The possible paths of the status of EIPs are as follows:

<img src=./eip-1/process.png>

Some Informational and Process EIPs may also have a status of “Active” if they are never meant to be completed. E.g. EIP 1 (this EIP).

What belongs in a successful EIP?
---------------------------------

Each EIP should have the following parts:

-   Preamble - RFC 822 style headers containing metadata about the EIP, including the EIP number, a short descriptive title (limited to a maximum of 44 characters), the names, and optionally the contact info for each author, etc.

<!-- -->

-   Simple Summary - “If you can’t explain it simply, you don’t understand it well enough.” Provide a simplified and layman-accessible explanation of the EIP.

<!-- -->

-   Abstract - a short (~200 word) description of the technical issue being addressed.

<!-- -->

-   Motivation (*optional) - The motivation is critical for EIPs that want to change the Ethereum protocol. It should clearly explain why the existing protocol specification is inadequate to address the problem that the EIP solves. EIP submissions without sufficient motivation may be rejected outright.

<!-- -->

-   Specification - The technical specification should describe the syntax and semantics of any new feature. The specification should be detailed enough to allow competing, interoperable implementations for any of the current Ethereum platforms (cpp-ethereum, go-ethereum, parity, ethereumJ, ethereumjs-lib, …).

<!-- -->

-   Rationale - The rationale fleshes out the specification by describing what motivated the design and why particular design decisions were made. It should describe alternate designs that were considered and related work, e.g. how the feature is supported in other languages. The rationale may also provide evidence of consensus within the community, and should discuss important objections or concerns raised during discussion.

<!-- -->

-   Backwards Compatibility - All EIPs that introduce backwards incompatibilities must include a section describing these incompatibilities and their severity. The EIP must explain how the author proposes to deal with these incompatibilities. EIP submissions without a sufficient backwards compatibility treatise may be rejected outright.

<!-- -->

-   Test Cases - Test cases for an implementation are mandatory for EIPs that are affecting consensus changes. Other EIPs can choose to include links to test cases if applicable.

<!-- -->

-   Implementations - The implementations must be completed before any EIP is given status “Final”, but it need not be completed before the EIP is accepted. While there is merit to the approach of reaching consensus on the specification and rationale before writing code, the principle of “rough consensus and running code” is still useful when it comes to resolving many discussions of API details.

EIP Formats and Templates
-------------------------

EIPs should be written in [markdown] format. Image files should be included in a subdirectory for that EIP.

EIP Header Preamble
-------------------

Each EIP must begin with an RFC 822 style header preamble. The headers must appear in the following order. Headers marked with "*" are optional and are described below. All other headers are required.

` EIP: ` <EIP number> (this is determined by the EIP editor)

` Title: `<EIP title>

` Author: `<list of author's real names and optionally, email address>

` * Discussions-To: ` <email address>

` Status: `<Draft | Active | Accepted | Deferred | Rejected | Withdrawn | Final | Superseded>

` Type: `<Standards Track (Core, Networking, Interface, ERC)  | Informational | Process>

` Created: `<date created on, in ISO 8601 (yyyy-mm-dd) format>

` * Replaces: `<EIP number>

` * Superseded-By: `<EIP number>

` * Resolution: `<url>

The Author header lists the names, and optionally the email addresses of all the authors/owners of the EIP. The format of the Author header value must be

Random J. User &lt;address@dom.ain&gt;

if the email address is included, and

Random J. User

if the email address is not given.

Note: The Resolution header is required for Standards Track EIPs only. It contains a URL that should point to an email message or other web resource where the pronouncement about the EIP is made.

While an EIP is in private discussions (usually during the initial Draft phase), a Discussions-To header will indicate the mailing list or URL where the EIP is being discussed. No Discussions-To header is necessary if the EIP is being discussed privately with the author.

The Type header specifies the type of EIP: Standards Track, Meta, or Informational. If the track is Standards please include the subcategory (core, networking, interface, or ERC).

The Created header records the date that the EIP was assigned a number. Both headers should be in yyyy-mm-dd format, e.g. 2001-08-14.

EIPs may have a Requires header, indicating the EIP numbers that this EIP depends on.

EIPs may also have a Superseded-By header indicating that an EIP has been rendered obsolete by a later document; the value is the number of the EIP that replaces the current document. The newer EIP must have a Replaces header containing the number of the EIP that it rendered obsolete.

Auxiliary Files
---------------

EIPs may include auxiliary files such as diagrams. Such files must be named EIP-XXXX-Y.ext, where “XXXX” is the EIP number, “Y” is a serial number (starting at 1), and “ext” is replaced by the actual file extension (e.g. “png”).

Transferring EIP Ownership
--------------------------

It occasionally becomes necessary to transfer ownership of EIPs to a new champion. In general, we'd like to retain the original author as a co-author of the transferred EIP, but that's really up to the original author. A good reason to transfer ownership is because the original author no longer has the time or interest in updating it or following through with the EIP process, or has fallen off the face of the 'net (i.e. is unreachable or not responding to email). A bad reason to transfer ownership is because you don't agree with the direction of the EIP. We try to build consensus around an EIP, but if that's not possible, you can always submit a competing EIP.

If you are interested in assuming ownership of an EIP, send a message asking to take over, addressed to both the original author and the EIP editor. If the original author doesn't respond to email in a timely manner, the EIP editor will make a unilateral decision (it's not like such decisions can't be reversed :).

EIP Editors
-----------

The current EIP editors are

` * Casey Detrio (@cdetrio)`

` * Fabian Vogelsteller (@frozeman)`

` * Gavin Wood (@gavofyork)`

` * Hudson Jameson (@Souptacular)`

` * Jeffrey Wilcke (@obscuren)`

` * Martin Becze (@wanderer)`

` * Nick Johnson (@arachnid)`

` * Roman Mandeleil (@romanman)`

` * Vitalik Buterin (@vbuterin)`

EIP Editor Responsibilities and Workflow
--------------------------------------

For each new EIP that comes in, an editor does the following:

-   Read the EIP to check if it is ready: sound and complete. The ideas must make technical sense, even if they don't seem likely to be accepted.
-   The title should accurately describe the content.
-   Edit the EIP for language (spelling, grammar, sentence structure, etc.), markup (Github flavored Markdown), code style

If the EIP isn't ready, the editor will send it back to the author for revision, with specific instructions.

Once the EIP is ready for the repository, the EIP editor will:

-   Assign an EIP number (generally the PR number or, if preferred by the author, the Issue # if there was discussion in the Issues section of this repository about this EIP)

<!-- -->

-   Accept the corresponding pull request

<!-- -->

-   List the EIP in [README.md]

<!-- -->

-   Send a message back to the EIP author with next step.

Many EIPs are written and maintained by developers with write access to the Ethereum codebase. The EIP editors monitor EIP changes, and correct any structure, grammar, spelling, or markup mistakes we see.

The editors don't pass judgment on EIPs. We merely do the administrative & editorial part.

History
-------

This document was derived heavily from [Bitcoin's BIP-0001] written by Amir Taaki which in turn was derived from [Python's PEP-0001]. In many places text was simply copied and modified. Although the PEP-0001 text was written by Barry Warsaw, Jeremy Hylton, and David Goodger, they are not responsible for its use in the Ethereum Improvement Process, and should not be bothered with technical questions specific to Ethereum or the EIP. Please direct all comments to the EIP editors.

December 7, 2016: EIP 1 has been improved and will be placed as a PR.

February 1, 2016: EIP 1 has added editors, made draft improvements to process, and has merged with Master stream.

  [EIP5]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-5.md
  [EIP101]: https://github.com/ethereum/EIPs/issues/28
  [EIP90]: https://github.com/ethereum/EIPs/issues/90
  [EIP86]: https://github.com/ethereum/EIPs/issues/86#issue-145324865
  [devp2p]: https://github.com/ethereum/wiki/wiki/%C3%90%CE%9EVp2p-Wire-Protocol
  [EIP8]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8.md
  [Light Ethereum Subprotocol]: https://github.com/ethereum/wiki/wiki/Light-client-protocol
  [whisper]: https://gist.github.com/gluk256/4654922ca45eb9d0846d941d7ca326f4
  [swarm]: https://github.com/ethereum/go-ethereum/pull/2959
  [API/RPC]: https://github.com/ethereum/wiki/wiki/JSON-RPC
  [EIP59]: https://github.com/ethereum/EIPs/issues/59
  [EIP6]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-6.md
  [contract ABIs]: https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI
  [interfaces repo]: https://github.com/ethereum/interfaces
  [ERC20]: https://github.com/ethereum/EIPs/issues/20
  [ERC26]: https://github.com/ethereum/EIPs/issues/26
  [ERC137]: https://github.com/ethereum/EIPs/issues/137
  [ERC67]: https://github.com/ethereum/EIPs/issues/67
  [EIP82]: https://github.com/ethereum/EIPs/issues/82
  [EIP75]: https://github.com/ethereum/EIPs/issues/75
  [EIP85]: https://github.com/ethereum/EIPs/issues/85
  [the Ethereum subreddit]: https://www.reddit.com/r/ethereum/
  [one of the Ethereum Gitter chat rooms]: https://gitter.im/ethereum/
  [pull request]: https://github.com/ethereum/EIPs/pulls
  [formal specification]: https://github.com/ethereum/yellowpaper
  [the Issues section of this repository]: https://github.com/ethereum/EIPs/issues
  [markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
  [README.md]: README.md "wikilink"
  [Bitcoin's BIP-0001]: https://github.com/bitcoin/bips
  [Python's PEP-0001]: https://www.python.org/dev/peps/


#eip-101.md
### Title

      EIP: 101
      Title: Serenity Currency and Crypto Abstraction
      Author: Vitalik Buterin <v@buterin.com>
      Status: Active
      Type: Serenity feature
      Created: 2015-11-15

### Specification

1.  Accounts now have only two fields in their RLP encoding: **code** and **storage**.
2.  Ether is no longer stored in account objects directly; instead, at address `0`, we premine a contract which contains all ether holdings. The `eth.getBalance` command in web3 is remapped appropriately.
3.  `msg.value` no longer exists as an opcode.
4.  A transaction now only has four fields: **to**, **startgas**, **data** and **code**.
5.  Aside from an RLP validity check, and checking that the **to** field is twenty bytes long, the **startgas** is an integer, and **code** is either empty or hashes to the **to** address, there are no other validity constraints; anything goes. However, the block gas limit remains, so miners are disincentivized from including junk.
6.  Gas is charged for bytes in **code** at the same rate as **data**.
7.  When a transaction is sent, if the receiving account does not yet exist, the account is created, and its code is set to the code provided in the transaction; otherwise the code is ignored.
8.  A `tx.gas` opcode is added alongside the existing `msg.gas` at index `0x5c`; this new opcode allows the transaction to access the original amount of gas allotted for the transaction

Note that `ECRECOVER`, sequence number/nonce incrementing and ether are now nowhere in the bottom-level spec (NOTE: ether is going to continue to have a privileged role in Casper PoS). To replicate existing functionality under the new model, we do the following.

Simple user accounts can have the following default standardized code:

```python
# We assume that data takes the following schema:
# bytes 0-31: v (ECDSA sig)
# bytes 32-63: r (ECDSA sig)
# bytes 64-95: s (ECDSA sig)
# bytes 96-127: sequence number (formerly called "nonce")
# bytes 128-159: gasprice
# bytes 172-191: to
# bytes 192+: data

# Get the hash for transaction signing
~mstore(0, msg.gas)
~calldatacopy(32, 96, ~calldatasize() - 96)
h = sha3(96, ~calldatasize() - 96)
# Call ECRECOVER contract to get the sender
~call(5000, 3, [h, ~calldataload(0), ~calldataload(32), ~calldataload(64)], 128, ref(addr), 32)
# Check sender correctness
assert addr == 0x82a978b3f5962a5b0957d9ee9eef472ee55b42f1
# Check sequence number correctness
assert ~calldataload(96) == self.storage[-1]
# Increment sequence number
self.storage[-1] += 1
# Make the sub-call and discard output
~call(msg.gas - 50000, ~calldataload(160), 192, ~calldatasize() - 192, 0, 0)
# Pay for gas
~call(40000, 0, [SEND, block.coinbase, ~calldataload(128) * (tx.gas - msg.gas + 50000)], 96, 0, 0)
```

This essentially implements signature and nonce checking, and if both checks pass then it uses all remaining gas minus 50000 to send the actual desired call, and then finally pays for gas.

Miners can follow the following algorithm upon receiving transactions:

1.  Run the code for a maximum of 50000 gas, stopping if they see an operation or call that threatens to go over this limit
2.  Upon seeing that operation, make sure that it leaves at last 50000 gas to spare (either by checking that the static gas consumption is small enough or by checking that it is a call with `msg.gas - 50000` as its gas limit parameter)
3.  Pattern-match to make sure that gas payment code at the end is *exactly* the same as in the code above.

This process ensures that miners *waste* at most 50000 gas before knowing whether or not it will be worth their while to include the transaction, and is also highly general so users can experiment with new cryptography (eg. ed25519, Lamport), ring signatures, quasi-native multisig, etc. Theoretically, one can even create an account for which the *valid signature* type is a valid Merkle branch of a receipt, creating a quasi-native alarm clock.

If someone wants to send a transaction with nonzero value, instead of the current `msg.sender` approach, we compile into a three step process:

1.  In the outer scope just before calling, call the ether contract to create a cheque for the desired amount
2.  In the inner scope, if a contract uses the `msg.value` opcode anywhere in the function that is being called, then we have the contract cash out the cheque at the start of the function call and store the amount cashed out in a standardized address in memory
3.  In the outer scope just after calling, send a message to the ether contract to disable the cheque if it has not yet been cashed

### Rationale

This allows for a large increase in generality, particularly in a few
areas:

1.  Cryptographic algorithms used to secure accounts (we could reasonably say that Ethereum is quantum-safe, as one is perfectly free to secure one's account with Lamport signatures). The nonce-incrementing approach is now also open to revision on the part of account holders, allowing for experimentation in k-parallelizable nonce techniques, UTXO schemes, etc.
2.  Moving ether up a level of abstraction, with the particular benefit of allowing ether and sub-tokens to be treated similarly by contracts
3.  Reducing the level of indirection required for custom-policy accounts such as multisigs

It also substantially simplifies and *purifies* the underlying Ethereum protocol, reducing the minimal consensus implementation complexity.

### Implementation

Coming soon.


#eip-107.md
<pre>
  EIP: 107
  Title: safe "eth_sendTransaction" authorization via html popup
  Author: Ronan Sandford <wighawag@gmail.com>
  Created: 2016-06-05
  Status: Draft
  Type: Standard
  Category: Interface
</pre>

Abstract
========
This draft EIP describes the details of an authorization method that if provided by rpc enabled ethereum nodes would allow regular websites to send transactions (via ```eth_sendTransaction```) without the need to enable CORS. Instead, user would be asked to confirm the transaction via an html popup. 

Every read only rpc call the dapp wants to perform is redirected to an invisible iframe from the node's domain and for every transaction that the dapp wish to execute, an html popup is presented to the user to allow him/her to cancel or confirm the transaction. This allows the dapp to connect to the node's rpc api without being  granted any kind of privileges. This allows users to safely interact with dapps running in their everyday web browser while their accounts are unlocked. In case the account is not unlocked, and the node has allowed the "personal" api via rpc,the html page also allow the user to enter their password to unlock the account for the scope of the transaction.

Motivation
==========
Currently, if a user navigates to a dapp running on a website using her/his everyday browser, the dapp will by default have no access to the rpc api for security reasons. The user will have to enable CORS for the website's domain in order for the dapp to work. Unfortunately if the user does so, the dapp will be able to send transactions from any unlocked account without the need for any user consent. In other words, not only does the user need to change the node's default setting, but the user is also forced to trust the dapp in order to use it. This is of course not acceptable and forces existing dapps to rely on the use of workarrounds like:
- if the transaction is a plain ether transfer, the user is asked to enter it in a dedicated trusted wallet like "Mist"
- For more complex case, the user is asked to enter the transaction manually via the node command line interface.


This proposal aims to provide a safe and user friendly alternative.

Here are some screenshots of the provided implementation of that html popup:

Account unlocked :
-----------------
When the account is already unlocked, the user is presented with the following popup for every transaction that the dapp attempts to make:

<img src="./eip-107/authorization.png">

Account locked and no "personal" api exposed via rpc:
-----------------
When the account is locked, and the node does not provide access to account unlocking via its rpc interface, the following popup will be presented. This is not ideal since this requires the user to know how to unlock an account:

<img src="./eip-107/authorization-locked.png">

Account locked but node exposing the "personal" api via rpc :
-----------------
A better option is to ask the user for their password, but this is only possible if the node allows access to the "personal" api via rpc. In such case, the following dialog will be presented to the user so he/she can accept the transaction by providing the password required to unlock the account:

<img src="./eip-107/authorization-password.png">


Specification
=============
In order for the mechanism to work, the node needs to serve an html file via http at the url \<node url\>/authorization.html

This file will then be used by the dapp in 2 different modes (invisible iframe and popup window).

The invisible iframe will be embeded in the dapp to allow the dapp to send its read-only rpc call without having to enable CORS for the dapp's website domain. This is done by sending message to the iframe (via javascript ```window.postMessage```) which in turn execute the rpc call. This works since the iframe and the node share the same domain/port. 

In the iframe mode, the html file's javascript code will ensure that no call requiring an unlocked key can be made. This is to prevent dapps from embedding the invisible iframe and tricking the user into clicking the confirm button.
If the dapp requires an ```eth_sendTransaction``` call, the dapp will instead open a new window using the same url.

In this popup window mode, the html file's javascript code will alow ```eth_sendTransaction``` (but not  ```eth_sign```, as there is no way to display to the user the meaningful content of the transaction to sign in a safe way) to be called. But instead of sending the call to the node directly, a confirmation dialog will be presented showing the sender and recipient addresses, as well as the amount being transfered along with the potential gas cost. Upon the user approving, the request will be sent and the result returned to the dapp. An error will be returned in case the user cancel the request. 

The html page also checks for the availability of the "personal" api and if so, will ask the user to unlock the account if necessary. The unlocking is temporary (3s) so the password will be asked again if a transaction is attempted before the end of this short time.

In both iframe mode and window mode, the communication with the dapp is achieved using ```window.postMessage```. 
The fist message the iframe/window sends is a message containing the string "ready" to let the dapp know that it now accepts messages. Then the dapp can start performing rpc call by sending message using the following object :
```
{
  id:<a an id>, //so responses can be match as there is no guarantee of the order of the response
  payload:<json rpc object> //this is the exact object that usually send to the node
}
```

For ```eth_sendTransaction``` the "gas", "gasPrice" and "from" field need to be set in the rpc parameter so that the window can display the correct value. If not all of these are passed in, the window will return an error.

Upon receiving such message, the iframe will perform the actual rpc call to the node but only if such a call is a read only call (not requiring an unlocked key). If it is not it will return a error. The window on the other will only accept ```eth_sendTransaction``` calls but will display a dialog so the user can accept or cancel the request.

In all the cases, the iframe/window will send a message back to the dapp using the following object:
```
{
  id:<id matchign the request>,
  result:<rpc result as is>,
  error:<error object>
}
```

the error object cannot be a javascript Error object due to postMessage limitation. Instead it is 
```
{
  message:<a string describing the error>,
  type:<a string defining the type of error> //type="cancel" means the user cancel the transaction
}
```


Rationale
=========
The design for that proposal was chosen for its simplicity and security. A previous idea was to use an oauth-like protocol in order for the user to accept or deny a transaction request. It would have required deeper code change in the node and some geth contributors argues that such change did not fit into geth code base as it would have required dapp aware code. 
The current design, instead has a very simple implementation (self contained html file that can be shared across node's implementation) and its safeness is guarantess by browsers' cross domain policies.

The use of iframe/ window was required to have both security and user friendliness. The invisble iframe allows the dapp to execute read only calls without the need for user input, and the window ensures user approval before making a call. While we could have made it without the window mode by making the iframe confirmation use the native browser ```window.confirm``` dialog, this would have prevented the use of a more elegant confirmation popup that the current design allows. It also happens to be that the ```window.confirm``` is not safe in some browsers, as it gives focus to the accept option and can be triggered automatically (https://bugs.chromium.org/p/chromium/issues/detail?id=260653).


Implementations
===============
In order to implement this design, the following html file or an equivalent one needs to be served at the url \<node url\>/authorization.html

That's it.


```
<!DOCTYPE html>
<html>
  <head>
    <title>Ethereum Authorization</title>
  </head>
  <script>
    //https://github.com/alexvandesande/blockies
    !function(){function r(r){for(var t=0;t<l.length;t++)l[t]=0;for(var t=0;t<r.length;t++)l[t%4]=(l[t%4]<<5)-l[t%4]+r.charCodeAt(t)}function t(){var r=l[0]^l[0]<<11;return l[0]=l[1],l[1]=l[2],l[2]=l[3],l[3]=l[3]^l[3]>>19^r^r>>8,(l[3]>>>0)/(1<<31>>>0)}function e(){var r=Math.floor(360*t()),e=60*t()+40+"%",o=25*(t()+t()+t()+t())+"%",n="hsl("+r+","+e+","+o+")";return n}function o(r){for(var e=r,o=r,n=Math.ceil(e/2),a=e-n,l=[],c=0;o>c;c++){for(var f=[],h=0;n>h;h++)f[h]=Math.floor(2.3*t());var i=f.slice(0,a);i.reverse(),f=f.concat(i);for(var v=0;v<f.length;v++)l.push(f[v])}return l}function n(r,t,e,o,n){var a=document.createElement("canvas"),l=Math.sqrt(r.length);a.width=a.height=l*e;var c=a.getContext("2d");c.fillStyle=o,c.fillRect(0,0,a.width,a.height),c.fillStyle=t;for(var f=0;f<r.length;f++){var h=Math.floor(f/l),i=f%l;c.fillStyle=1==r[f]?t:n,r[f]&&c.fillRect(i*e,h*e,e,e)}return a}function a(t){t=t||{};var a=t.size||8,l=t.scale||4,c=t.seed||Math.floor(Math.random()*Math.pow(10,16)).toString(16);r(c);var f=t.color||e(),h=t.bgcolor||e(),i=t.spotcolor||e(),v=o(a),u=n(v,f,l,h,i);return u}var l=new Array(4);window.blockies={create:a}}();
    
    /* bignumber.js v2.3.0 https://github.com/MikeMcl/bignumber.js/LICENCE */
    !function(e){"use strict";function n(e){function E(e,n){var t,r,i,o,u,s,f=this;if(!(f instanceof E))return j&&L(26,"constructor call without new",e),new E(e,n);if(null!=n&&H(n,2,64,M,"base")){if(n=0|n,s=e+"",10==n)return f=new E(e instanceof E?e:s),U(f,P+f.e+1,k);if((o="number"==typeof e)&&0*e!=0||!new RegExp("^-?"+(t="["+N.slice(0,n)+"]+")+"(?:\\."+t+")?$",37>n?"i":"").test(s))return h(f,s,o,n);o?(f.s=0>1/e?(s=s.slice(1),-1):1,j&&s.replace(/^0\.0*|\./,"").length>15&&L(M,v,e),o=!1):f.s=45===s.charCodeAt(0)?(s=s.slice(1),-1):1,s=D(s,10,n,f.s)}else{if(e instanceof E)return f.s=e.s,f.e=e.e,f.c=(e=e.c)?e.slice():e,void(M=0);if((o="number"==typeof e)&&0*e==0){if(f.s=0>1/e?(e=-e,-1):1,e===~~e){for(r=0,i=e;i>=10;i/=10,r++);return f.e=r,f.c=[e],void(M=0)}s=e+""}else{if(!g.test(s=e+""))return h(f,s,o);f.s=45===s.charCodeAt(0)?(s=s.slice(1),-1):1}}for((r=s.indexOf("."))>-1&&(s=s.replace(".","")),(i=s.search(/e/i))>0?(0>r&&(r=i),r+=+s.slice(i+1),s=s.substring(0,i)):0>r&&(r=s.length),i=0;48===s.charCodeAt(i);i++);for(u=s.length;48===s.charCodeAt(--u););if(s=s.slice(i,u+1))if(u=s.length,o&&j&&u>15&&(e>y||e!==d(e))&&L(M,v,f.s*e),r=r-i-1,r>z)f.c=f.e=null;else if(G>r)f.c=[f.e=0];else{if(f.e=r,f.c=[],i=(r+1)%O,0>r&&(i+=O),u>i){for(i&&f.c.push(+s.slice(0,i)),u-=O;u>i;)f.c.push(+s.slice(i,i+=O));s=s.slice(i),i=O-s.length}else i-=u;for(;i--;s+="0");f.c.push(+s)}else f.c=[f.e=0];M=0}function D(e,n,t,i){var o,u,f,c,a,h,g,p=e.indexOf("."),d=P,m=k;for(37>t&&(e=e.toLowerCase()),p>=0&&(f=J,J=0,e=e.replace(".",""),g=new E(t),a=g.pow(e.length-p),J=f,g.c=s(l(r(a.c),a.e),10,n),g.e=g.c.length),h=s(e,t,n),u=f=h.length;0==h[--f];h.pop());if(!h[0])return"0";if(0>p?--u:(a.c=h,a.e=u,a.s=i,a=C(a,g,d,m,n),h=a.c,c=a.r,u=a.e),o=u+d+1,p=h[o],f=n/2,c=c||0>o||null!=h[o+1],c=4>m?(null!=p||c)&&(0==m||m==(a.s<0?3:2)):p>f||p==f&&(4==m||c||6==m&&1&h[o-1]||m==(a.s<0?8:7)),1>o||!h[0])e=c?l("1",-d):"0";else{if(h.length=o,c)for(--n;++h[--o]>n;)h[o]=0,o||(++u,h.unshift(1));for(f=h.length;!h[--f];);for(p=0,e="";f>=p;e+=N.charAt(h[p++]));e=l(e,u)}return e}function F(e,n,t,i){var o,u,s,c,a;if(t=null!=t&&H(t,0,8,i,w)?0|t:k,!e.c)return e.toString();if(o=e.c[0],s=e.e,null==n)a=r(e.c),a=19==i||24==i&&B>=s?f(a,s):l(a,s);else if(e=U(new E(e),n,t),u=e.e,a=r(e.c),c=a.length,19==i||24==i&&(u>=n||B>=u)){for(;n>c;a+="0",c++);a=f(a,u)}else if(n-=s,a=l(a,u),u+1>c){if(--n>0)for(a+=".";n--;a+="0");}else if(n+=u-c,n>0)for(u+1==c&&(a+=".");n--;a+="0");return e.s<0&&o?"-"+a:a}function _(e,n){var t,r,i=0;for(u(e[0])&&(e=e[0]),t=new E(e[0]);++i<e.length;){if(r=new E(e[i]),!r.s){t=r;break}n.call(t,r)&&(t=r)}return t}function x(e,n,t,r,i){return(n>e||e>t||e!=c(e))&&L(r,(i||"decimal places")+(n>e||e>t?" out of range":" not an integer"),e),!0}function I(e,n,t){for(var r=1,i=n.length;!n[--i];n.pop());for(i=n[0];i>=10;i/=10,r++);return(t=r+t*O-1)>z?e.c=e.e=null:G>t?e.c=[e.e=0]:(e.e=t,e.c=n),e}function L(e,n,t){var r=new Error(["new BigNumber","cmp","config","div","divToInt","eq","gt","gte","lt","lte","minus","mod","plus","precision","random","round","shift","times","toDigits","toExponential","toFixed","toFormat","toFraction","pow","toPrecision","toString","BigNumber"][e]+"() "+n+": "+t);throw r.name="BigNumber Error",M=0,r}function U(e,n,t,r){var i,o,u,s,f,l,c,a=e.c,h=S;if(a){e:{for(i=1,s=a[0];s>=10;s/=10,i++);if(o=n-i,0>o)o+=O,u=n,f=a[l=0],c=f/h[i-u-1]%10|0;else if(l=p((o+1)/O),l>=a.length){if(!r)break e;for(;a.length<=l;a.push(0));f=c=0,i=1,o%=O,u=o-O+1}else{for(f=s=a[l],i=1;s>=10;s/=10,i++);o%=O,u=o-O+i,c=0>u?0:f/h[i-u-1]%10|0}if(r=r||0>n||null!=a[l+1]||(0>u?f:f%h[i-u-1]),r=4>t?(c||r)&&(0==t||t==(e.s<0?3:2)):c>5||5==c&&(4==t||r||6==t&&(o>0?u>0?f/h[i-u]:0:a[l-1])%10&1||t==(e.s<0?8:7)),1>n||!a[0])return a.length=0,r?(n-=e.e+1,a[0]=h[(O-n%O)%O],e.e=-n||0):a[0]=e.e=0,e;if(0==o?(a.length=l,s=1,l--):(a.length=l+1,s=h[O-o],a[l]=u>0?d(f/h[i-u]%h[u])*s:0),r)for(;;){if(0==l){for(o=1,u=a[0];u>=10;u/=10,o++);for(u=a[0]+=s,s=1;u>=10;u/=10,s++);o!=s&&(e.e++,a[0]==b&&(a[0]=1));break}if(a[l]+=s,a[l]!=b)break;a[l--]=0,s=1}for(o=a.length;0===a[--o];a.pop());}e.e>z?e.c=e.e=null:e.e<G&&(e.c=[e.e=0])}return e}var C,M=0,T=E.prototype,q=new E(1),P=20,k=4,B=-7,$=21,G=-1e7,z=1e7,j=!0,H=x,V=!1,W=1,J=100,X={decimalSeparator:".",groupSeparator:",",groupSize:3,secondaryGroupSize:0,fractionGroupSeparator:" ",fractionGroupSize:0};return E.another=n,E.ROUND_UP=0,E.ROUND_DOWN=1,E.ROUND_CEIL=2,E.ROUND_FLOOR=3,E.ROUND_HALF_UP=4,E.ROUND_HALF_DOWN=5,E.ROUND_HALF_EVEN=6,E.ROUND_HALF_CEIL=7,E.ROUND_HALF_FLOOR=8,E.EUCLID=9,E.config=function(){var e,n,t=0,r={},i=arguments,s=i[0],f=s&&"object"==typeof s?function(){return s.hasOwnProperty(n)?null!=(e=s[n]):void 0}:function(){return i.length>t?null!=(e=i[t++]):void 0};return f(n="DECIMAL_PLACES")&&H(e,0,A,2,n)&&(P=0|e),r[n]=P,f(n="ROUNDING_MODE")&&H(e,0,8,2,n)&&(k=0|e),r[n]=k,f(n="EXPONENTIAL_AT")&&(u(e)?H(e[0],-A,0,2,n)&&H(e[1],0,A,2,n)&&(B=0|e[0],$=0|e[1]):H(e,-A,A,2,n)&&(B=-($=0|(0>e?-e:e)))),r[n]=[B,$],f(n="RANGE")&&(u(e)?H(e[0],-A,-1,2,n)&&H(e[1],1,A,2,n)&&(G=0|e[0],z=0|e[1]):H(e,-A,A,2,n)&&(0|e?G=-(z=0|(0>e?-e:e)):j&&L(2,n+" cannot be zero",e))),r[n]=[G,z],f(n="ERRORS")&&(e===!!e||1===e||0===e?(M=0,H=(j=!!e)?x:o):j&&L(2,n+m,e)),r[n]=j,f(n="CRYPTO")&&(e===!!e||1===e||0===e?(V=!(!e||!a),e&&!V&&j&&L(2,"crypto unavailable",a)):j&&L(2,n+m,e)),r[n]=V,f(n="MODULO_MODE")&&H(e,0,9,2,n)&&(W=0|e),r[n]=W,f(n="POW_PRECISION")&&H(e,0,A,2,n)&&(J=0|e),r[n]=J,f(n="FORMAT")&&("object"==typeof e?X=e:j&&L(2,n+" not an object",e)),r[n]=X,r},E.max=function(){return _(arguments,T.lt)},E.min=function(){return _(arguments,T.gt)},E.random=function(){var e=9007199254740992,n=Math.random()*e&2097151?function(){return d(Math.random()*e)}:function(){return 8388608*(1073741824*Math.random()|0)+(8388608*Math.random()|0)};return function(e){var t,r,i,o,u,s=0,f=[],l=new E(q);if(e=null!=e&&H(e,0,A,14)?0|e:P,o=p(e/O),V)if(a&&a.getRandomValues){for(t=a.getRandomValues(new Uint32Array(o*=2));o>s;)u=131072*t[s]+(t[s+1]>>>11),u>=9e15?(r=a.getRandomValues(new Uint32Array(2)),t[s]=r[0],t[s+1]=r[1]):(f.push(u%1e14),s+=2);s=o/2}else if(a&&a.randomBytes){for(t=a.randomBytes(o*=7);o>s;)u=281474976710656*(31&t[s])+1099511627776*t[s+1]+4294967296*t[s+2]+16777216*t[s+3]+(t[s+4]<<16)+(t[s+5]<<8)+t[s+6],u>=9e15?a.randomBytes(7).copy(t,s):(f.push(u%1e14),s+=7);s=o/7}else j&&L(14,"crypto unavailable",a);if(!s)for(;o>s;)u=n(),9e15>u&&(f[s++]=u%1e14);for(o=f[--s],e%=O,o&&e&&(u=S[O-e],f[s]=d(o/u)*u);0===f[s];f.pop(),s--);if(0>s)f=[i=0];else{for(i=-1;0===f[0];f.shift(),i-=O);for(s=1,u=f[0];u>=10;u/=10,s++);O>s&&(i-=O-s)}return l.e=i,l.c=f,l}}(),C=function(){function e(e,n,t){var r,i,o,u,s=0,f=e.length,l=n%R,c=n/R|0;for(e=e.slice();f--;)o=e[f]%R,u=e[f]/R|0,r=c*o+u*l,i=l*o+r%R*R+s,s=(i/t|0)+(r/R|0)+c*u,e[f]=i%t;return s&&e.unshift(s),e}function n(e,n,t,r){var i,o;if(t!=r)o=t>r?1:-1;else for(i=o=0;t>i;i++)if(e[i]!=n[i]){o=e[i]>n[i]?1:-1;break}return o}function r(e,n,t,r){for(var i=0;t--;)e[t]-=i,i=e[t]<n[t]?1:0,e[t]=i*r+e[t]-n[t];for(;!e[0]&&e.length>1;e.shift());}return function(i,o,u,s,f){var l,c,a,h,g,p,m,w,v,N,y,S,R,A,D,F,_,x=i.s==o.s?1:-1,I=i.c,L=o.c;if(!(I&&I[0]&&L&&L[0]))return new E(i.s&&o.s&&(I?!L||I[0]!=L[0]:L)?I&&0==I[0]||!L?0*x:x/0:NaN);for(w=new E(x),v=w.c=[],c=i.e-o.e,x=u+c+1,f||(f=b,c=t(i.e/O)-t(o.e/O),x=x/O|0),a=0;L[a]==(I[a]||0);a++);if(L[a]>(I[a]||0)&&c--,0>x)v.push(1),h=!0;else{for(A=I.length,F=L.length,a=0,x+=2,g=d(f/(L[0]+1)),g>1&&(L=e(L,g,f),I=e(I,g,f),F=L.length,A=I.length),R=F,N=I.slice(0,F),y=N.length;F>y;N[y++]=0);_=L.slice(),_.unshift(0),D=L[0],L[1]>=f/2&&D++;do{if(g=0,l=n(L,N,F,y),0>l){if(S=N[0],F!=y&&(S=S*f+(N[1]||0)),g=d(S/D),g>1)for(g>=f&&(g=f-1),p=e(L,g,f),m=p.length,y=N.length;1==n(p,N,m,y);)g--,r(p,m>F?_:L,m,f),m=p.length,l=1;else 0==g&&(l=g=1),p=L.slice(),m=p.length;if(y>m&&p.unshift(0),r(N,p,y,f),y=N.length,-1==l)for(;n(L,N,F,y)<1;)g++,r(N,y>F?_:L,y,f),y=N.length}else 0===l&&(g++,N=[0]);v[a++]=g,N[0]?N[y++]=I[R]||0:(N=[I[R]],y=1)}while((R++<A||null!=N[0])&&x--);h=null!=N[0],v[0]||v.shift()}if(f==b){for(a=1,x=v[0];x>=10;x/=10,a++);U(w,u+(w.e=a+c*O-1)+1,s,h)}else w.e=c,w.r=+h;return w}}(),h=function(){var e=/^(-?)0([xbo])(?=\w[\w.]*$)/i,n=/^([^.]+)\.$/,t=/^\.([^.]+)$/,r=/^-?(Infinity|NaN)$/,i=/^\s*\+(?=[\w.])|^\s+|\s+$/g;return function(o,u,s,f){var l,c=s?u:u.replace(i,"");if(r.test(c))o.s=isNaN(c)?null:0>c?-1:1;else{if(!s&&(c=c.replace(e,function(e,n,t){return l="x"==(t=t.toLowerCase())?16:"b"==t?2:8,f&&f!=l?e:n}),f&&(l=f,c=c.replace(n,"$1").replace(t,"0.$1")),u!=c))return new E(c,l);j&&L(M,"not a"+(f?" base "+f:"")+" number",u),o.s=null}o.c=o.e=null,M=0}}(),T.absoluteValue=T.abs=function(){var e=new E(this);return e.s<0&&(e.s=1),e},T.ceil=function(){return U(new E(this),this.e+1,2)},T.comparedTo=T.cmp=function(e,n){return M=1,i(this,new E(e,n))},T.decimalPlaces=T.dp=function(){var e,n,r=this.c;if(!r)return null;if(e=((n=r.length-1)-t(this.e/O))*O,n=r[n])for(;n%10==0;n/=10,e--);return 0>e&&(e=0),e},T.dividedBy=T.div=function(e,n){return M=3,C(this,new E(e,n),P,k)},T.dividedToIntegerBy=T.divToInt=function(e,n){return M=4,C(this,new E(e,n),0,1)},T.equals=T.eq=function(e,n){return M=5,0===i(this,new E(e,n))},T.floor=function(){return U(new E(this),this.e+1,3)},T.greaterThan=T.gt=function(e,n){return M=6,i(this,new E(e,n))>0},T.greaterThanOrEqualTo=T.gte=function(e,n){return M=7,1===(n=i(this,new E(e,n)))||0===n},T.isFinite=function(){return!!this.c},T.isInteger=T.isInt=function(){return!!this.c&&t(this.e/O)>this.c.length-2},T.isNaN=function(){return!this.s},T.isNegative=T.isNeg=function(){return this.s<0},T.isZero=function(){return!!this.c&&0==this.c[0]},T.lessThan=T.lt=function(e,n){return M=8,i(this,new E(e,n))<0},T.lessThanOrEqualTo=T.lte=function(e,n){return M=9,-1===(n=i(this,new E(e,n)))||0===n},T.minus=T.sub=function(e,n){var r,i,o,u,s=this,f=s.s;if(M=10,e=new E(e,n),n=e.s,!f||!n)return new E(NaN);if(f!=n)return e.s=-n,s.plus(e);var l=s.e/O,c=e.e/O,a=s.c,h=e.c;if(!l||!c){if(!a||!h)return a?(e.s=-n,e):new E(h?s:NaN);if(!a[0]||!h[0])return h[0]?(e.s=-n,e):new E(a[0]?s:3==k?-0:0)}if(l=t(l),c=t(c),a=a.slice(),f=l-c){for((u=0>f)?(f=-f,o=a):(c=l,o=h),o.reverse(),n=f;n--;o.push(0));o.reverse()}else for(i=(u=(f=a.length)<(n=h.length))?f:n,f=n=0;i>n;n++)if(a[n]!=h[n]){u=a[n]<h[n];break}if(u&&(o=a,a=h,h=o,e.s=-e.s),n=(i=h.length)-(r=a.length),n>0)for(;n--;a[r++]=0);for(n=b-1;i>f;){if(a[--i]<h[i]){for(r=i;r&&!a[--r];a[r]=n);--a[r],a[i]+=b}a[i]-=h[i]}for(;0==a[0];a.shift(),--c);return a[0]?I(e,a,c):(e.s=3==k?-1:1,e.c=[e.e=0],e)},T.modulo=T.mod=function(e,n){var t,r,i=this;return M=11,e=new E(e,n),!i.c||!e.s||e.c&&!e.c[0]?new E(NaN):!e.c||i.c&&!i.c[0]?new E(i):(9==W?(r=e.s,e.s=1,t=C(i,e,0,3),e.s=r,t.s*=r):t=C(i,e,0,W),i.minus(t.times(e)))},T.negated=T.neg=function(){var e=new E(this);return e.s=-e.s||null,e},T.plus=T.add=function(e,n){var r,i=this,o=i.s;if(M=12,e=new E(e,n),n=e.s,!o||!n)return new E(NaN);if(o!=n)return e.s=-n,i.minus(e);var u=i.e/O,s=e.e/O,f=i.c,l=e.c;if(!u||!s){if(!f||!l)return new E(o/0);if(!f[0]||!l[0])return l[0]?e:new E(f[0]?i:0*o)}if(u=t(u),s=t(s),f=f.slice(),o=u-s){for(o>0?(s=u,r=l):(o=-o,r=f),r.reverse();o--;r.push(0));r.reverse()}for(o=f.length,n=l.length,0>o-n&&(r=l,l=f,f=r,n=o),o=0;n;)o=(f[--n]=f[n]+l[n]+o)/b|0,f[n]%=b;return o&&(f.unshift(o),++s),I(e,f,s)},T.precision=T.sd=function(e){var n,t,r=this,i=r.c;if(null!=e&&e!==!!e&&1!==e&&0!==e&&(j&&L(13,"argument"+m,e),e!=!!e&&(e=null)),!i)return null;if(t=i.length-1,n=t*O+1,t=i[t]){for(;t%10==0;t/=10,n--);for(t=i[0];t>=10;t/=10,n++);}return e&&r.e+1>n&&(n=r.e+1),n},T.round=function(e,n){var t=new E(this);return(null==e||H(e,0,A,15))&&U(t,~~e+this.e+1,null!=n&&H(n,0,8,15,w)?0|n:k),t},T.shift=function(e){var n=this;return H(e,-y,y,16,"argument")?n.times("1e"+c(e)):new E(n.c&&n.c[0]&&(-y>e||e>y)?n.s*(0>e?0:1/0):n)},T.squareRoot=T.sqrt=function(){var e,n,i,o,u,s=this,f=s.c,l=s.s,c=s.e,a=P+4,h=new E("0.5");if(1!==l||!f||!f[0])return new E(!l||0>l&&(!f||f[0])?NaN:f?s:1/0);if(l=Math.sqrt(+s),0==l||l==1/0?(n=r(f),(n.length+c)%2==0&&(n+="0"),l=Math.sqrt(n),c=t((c+1)/2)-(0>c||c%2),l==1/0?n="1e"+c:(n=l.toExponential(),n=n.slice(0,n.indexOf("e")+1)+c),i=new E(n)):i=new E(l+""),i.c[0])for(c=i.e,l=c+a,3>l&&(l=0);;)if(u=i,i=h.times(u.plus(C(s,u,a,1))),r(u.c).slice(0,l)===(n=r(i.c)).slice(0,l)){if(i.e<c&&--l,n=n.slice(l-3,l+1),"9999"!=n&&(o||"4999"!=n)){(!+n||!+n.slice(1)&&"5"==n.charAt(0))&&(U(i,i.e+P+2,1),e=!i.times(i).eq(s));break}if(!o&&(U(u,u.e+P+2,0),u.times(u).eq(s))){i=u;break}a+=4,l+=4,o=1}return U(i,i.e+P+1,k,e)},T.times=T.mul=function(e,n){var r,i,o,u,s,f,l,c,a,h,g,p,d,m,w,v=this,N=v.c,y=(M=17,e=new E(e,n)).c;if(!(N&&y&&N[0]&&y[0]))return!v.s||!e.s||N&&!N[0]&&!y||y&&!y[0]&&!N?e.c=e.e=e.s=null:(e.s*=v.s,N&&y?(e.c=[0],e.e=0):e.c=e.e=null),e;for(i=t(v.e/O)+t(e.e/O),e.s*=v.s,l=N.length,h=y.length,h>l&&(d=N,N=y,y=d,o=l,l=h,h=o),o=l+h,d=[];o--;d.push(0));for(m=b,w=R,o=h;--o>=0;){for(r=0,g=y[o]%w,p=y[o]/w|0,s=l,u=o+s;u>o;)c=N[--s]%w,a=N[s]/w|0,f=p*c+a*g,c=g*c+f%w*w+d[u]+r,r=(c/m|0)+(f/w|0)+p*a,d[u--]=c%m;d[u]=r}return r?++i:d.shift(),I(e,d,i)},T.toDigits=function(e,n){var t=new E(this);return e=null!=e&&H(e,1,A,18,"precision")?0|e:null,n=null!=n&&H(n,0,8,18,w)?0|n:k,e?U(t,e,n):t},T.toExponential=function(e,n){return F(this,null!=e&&H(e,0,A,19)?~~e+1:null,n,19)},T.toFixed=function(e,n){return F(this,null!=e&&H(e,0,A,20)?~~e+this.e+1:null,n,20)},T.toFormat=function(e,n){var t=F(this,null!=e&&H(e,0,A,21)?~~e+this.e+1:null,n,21);if(this.c){var r,i=t.split("."),o=+X.groupSize,u=+X.secondaryGroupSize,s=X.groupSeparator,f=i[0],l=i[1],c=this.s<0,a=c?f.slice(1):f,h=a.length;if(u&&(r=o,o=u,u=r,h-=r),o>0&&h>0){for(r=h%o||o,f=a.substr(0,r);h>r;r+=o)f+=s+a.substr(r,o);u>0&&(f+=s+a.slice(r)),c&&(f="-"+f)}t=l?f+X.decimalSeparator+((u=+X.fractionGroupSize)?l.replace(new RegExp("\\d{"+u+"}\\B","g"),"$&"+X.fractionGroupSeparator):l):f}return t},T.toFraction=function(e){var n,t,i,o,u,s,f,l,c,a=j,h=this,g=h.c,p=new E(q),d=t=new E(q),m=f=new E(q);if(null!=e&&(j=!1,s=new E(e),j=a,(!(a=s.isInt())||s.lt(q))&&(j&&L(22,"max denominator "+(a?"out of range":"not an integer"),e),e=!a&&s.c&&U(s,s.e+1,1).gte(q)?s:null)),!g)return h.toString();for(c=r(g),o=p.e=c.length-h.e-1,p.c[0]=S[(u=o%O)<0?O+u:u],e=!e||s.cmp(p)>0?o>0?p:d:s,u=z,z=1/0,s=new E(c),f.c[0]=0;l=C(s,p,0,1),i=t.plus(l.times(m)),1!=i.cmp(e);)t=m,m=i,d=f.plus(l.times(i=d)),f=i,p=s.minus(l.times(i=p)),s=i;return i=C(e.minus(t),m,0,1),f=f.plus(i.times(d)),t=t.plus(i.times(m)),f.s=d.s=h.s,o*=2,n=C(d,m,o,k).minus(h).abs().cmp(C(f,t,o,k).minus(h).abs())<1?[d.toString(),m.toString()]:[f.toString(),t.toString()],z=u,n},T.toNumber=function(){return+this},T.toPower=T.pow=function(e,n){var t,r,i,o=d(0>e?-e:+e),u=this;if(null!=n&&(M=23,n=new E(n)),!H(e,-y,y,23,"exponent")&&(!isFinite(e)||o>y&&(e/=0)||parseFloat(e)!=e&&!(e=NaN))||0==e)return t=Math.pow(+u,e),new E(n?t%n:t);for(n?e>1&&u.gt(q)&&u.isInt()&&n.gt(q)&&n.isInt()?u=u.mod(n):(i=n,n=null):J&&(t=p(J/O+2)),r=new E(q);;){if(o%2){if(r=r.times(u),!r.c)break;t?r.c.length>t&&(r.c.length=t):n&&(r=r.mod(n))}if(o=d(o/2),!o)break;u=u.times(u),t?u.c&&u.c.length>t&&(u.c.length=t):n&&(u=u.mod(n))}return n?r:(0>e&&(r=q.div(r)),i?r.mod(i):t?U(r,J,k):r)},T.toPrecision=function(e,n){return F(this,null!=e&&H(e,1,A,24,"precision")?0|e:null,n,24)},T.toString=function(e){var n,t=this,i=t.s,o=t.e;return null===o?i?(n="Infinity",0>i&&(n="-"+n)):n="NaN":(n=r(t.c),n=null!=e&&H(e,2,64,25,"base")?D(l(n,o),0|e,10,i):B>=o||o>=$?f(n,o):l(n,o),0>i&&t.c[0]&&(n="-"+n)),n},T.truncated=T.trunc=function(){return U(new E(this),this.e+1,1)},T.valueOf=T.toJSON=function(){var e,n=this,t=n.e;return null===t?n.toString():(e=r(n.c),e=B>=t||t>=$?f(e,t):l(e,t),n.s<0?"-"+e:e)},null!=e&&E.config(e),E}function t(e){var n=0|e;return e>0||e===n?n:n-1}function r(e){for(var n,t,r=1,i=e.length,o=e[0]+"";i>r;){for(n=e[r++]+"",t=O-n.length;t--;n="0"+n);o+=n}for(i=o.length;48===o.charCodeAt(--i););return o.slice(0,i+1||1)}function i(e,n){var t,r,i=e.c,o=n.c,u=e.s,s=n.s,f=e.e,l=n.e;if(!u||!s)return null;if(t=i&&!i[0],r=o&&!o[0],t||r)return t?r?0:-s:u;if(u!=s)return u;if(t=0>u,r=f==l,!i||!o)return r?0:!i^t?1:-1;if(!r)return f>l^t?1:-1;for(s=(f=i.length)<(l=o.length)?f:l,u=0;s>u;u++)if(i[u]!=o[u])return i[u]>o[u]^t?1:-1;return f==l?0:f>l^t?1:-1}function o(e,n,t){return(e=c(e))>=n&&t>=e}function u(e){return"[object Array]"==Object.prototype.toString.call(e)}function s(e,n,t){for(var r,i,o=[0],u=0,s=e.length;s>u;){for(i=o.length;i--;o[i]*=n);for(o[r=0]+=N.indexOf(e.charAt(u++));r<o.length;r++)o[r]>t-1&&(null==o[r+1]&&(o[r+1]=0),o[r+1]+=o[r]/t|0,o[r]%=t)}return o.reverse()}function f(e,n){return(e.length>1?e.charAt(0)+"."+e.slice(1):e)+(0>n?"e":"e+")+n}function l(e,n){var t,r;if(0>n){for(r="0.";++n;r+="0");e=r+e}else if(t=e.length,++n>t){for(r="0",n-=t;--n;r+="0");e+=r}else t>n&&(e=e.slice(0,n)+"."+e.slice(n));return e}function c(e){return e=parseFloat(e),0>e?p(e):d(e)}var a,h,g=/^-?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?$/i,p=Math.ceil,d=Math.floor,m=" not a boolean or binary digit",w="rounding mode",v="number type has more than 15 significant digits",N="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$_",b=1e14,O=14,y=9007199254740991,S=[1,10,100,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12,1e13],R=1e7,A=1e9;if("undefined"!=typeof crypto&&(a=crypto),"function"==typeof define&&define.amd)define(function(){return n()});else if("undefined"!=typeof module&&module.exports){if(module.exports=n(),!a)try{a=require("crypto")}catch(E){}}else e||(e="undefined"!=typeof self?self:Function("return this")()),e.BigNumber=n()}(this);
  </script>
  
  <style>
    body{
      font-family: 'HelveticaNeue-Light', 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', 'Lucida Grande', sans-serif;
      background: #E2E2E2;
    }
    *, *:after, *:before {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    #pleasewait{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
    }
    #infomessage {
      text-align: center;
      font-size: 1rem;
      margin: 0 2rem 4.5rem;
    }
    
    .wrapper{
      background: #E2E2E2;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      display:none;
      text-align: center;
    }
    .title {
      text-align: center;
      font-size: 1.2rem;
      margin: 1rem 0rem;
    }
    .message {
      text-align: center;
      font-size: 1rem;
      /*margin: 0 2rem 4.5rem;*/
    }
    
    #passwordField {
      text-align: center;
      font-size: 1rem;
      margin: 1rem 0rem;
      /*margin: 0 2rem 4.5rem;*/
    }
    
    .wrapper button {
      background: transparent;
      border: none;
      color: #1678E5;
      height: 3rem;
      font-size: 1rem;
      width: 50%;
      position: absolute;
      bottom: 0;
      cursor: pointer;
    }
    #cancel-button {
      border-top: 1px solid #B4B4B4;
      border-right: 1px solid #B4B4B4;
      left: 0;
      border-radius: 0 0 0 10px;
    }
    #confirm-button {
      border-top: 1px solid #B4B4B4;
      right: 0;
      border-radius: 0 0 10px 0;
    }
    .wrapper button:focus,
    .wrapper button:hover {
      font-weight: bold;
      background: #EFEFEF;
    }
    .wrapper button:active {
      background: #D6D6D6;
    }
    
    .button {
      margin: 1rem 0rem;
      display: inline-block;
      padding: 9px 15px;
      background-color: #3898EC;
      color: white;
      border: 0;
      line-height: inherit;
      text-decoration: none;
      cursor: pointer;
      border-radius: 0;
    }

    input.button {
      -webkit-appearance: button;
    }
  </style>
  
  <body>

    <div id="pleasewait">
      <br/>
      <p id="infomessage">Please wait...</p>
    </div>
    
    <form id="form" class="wrapper">
      <br/>
      <p id="message" class="message"></p>
      <p id="passwordField"><label>Password Required:</label><input id="password" type="password" /></p>
      <button id="cancel-button" type="button" autofocus>Cancel</button>
      <button id="confirm-button" type="button" >Confirm</button>
    </form>
  
    <div id="modal-dialog" class="wrapper">
      <h3 id="modal-dialog-title" class="title">Title</h3>
      <p id="modal-dialog-message" class="message">Message</p>
      <span id="modal-dialog-button" class="button">Ok</span>
    </div>
      
    <script>
    var noMessageReceivedYet = true;
    var closedByCode = false;
    var pleaseWait = document.getElementById("pleasewait");
    var form = document.getElementById("form");
    var cancelButton = document.getElementById("cancel-button");
    var confirmButton = document.getElementById("confirm-button");
    var message = document.getElementById("message");
    var infoMessage = document.getElementById("infomessage");
    var password = document.getElementById("password");
    var passwordField = document.getElementById("passwordField");
    var modalDialog = document.getElementById("modal-dialog");
    var modalDialogButton = document.getElementById("modal-dialog-button");
    var modalDialogTitle = document.getElementById("modal-dialog-title");
    var modalDialogMessage = document.getElementById("modal-dialog-message");
    
    var firstUrl = null;
    
    var inIframe = true;
    var source = null;
    if(window.opener){
      inIframe = false;
      source = window.opener;
    }else if(window.parent != window){
      source = window.parent;
    }else{
      console.log("closing");
      window.close();
    }
    
    function closeWindow(){
      closedByCode = true;
      window.close();
    }
    
    function showWaiting(text){
      if(!text){
        text = "Please wait..."
      }
      infoMessage.innerHTML = text;
      pleaseWait.style.display = "block";
      form.style.display = "none";
    }
    
    function hideWaiting(){
      pleaseWait.style.display = "none";
      form.style.display = "block";
      
      window.onbeforeunload = null;
    }
      
    function showMessage(title, message, callback, buttonText){
      modalDialog.style.display = "block";
      modalDialogTitle.innerHTML = title;
      modalDialogMessage.innerHTML = "";
      if((typeof message) == "string"){
        modalDialogMessage.innerHTML += message;
      }else{
        modalDialogMessage.appendChild(message);
      }
      modalDialogMessage.appendChild(document.createElement('br'));
      
      if(!buttonText){
        buttonText = "Ok";
      }
      modalDialogButton.innerHTML = buttonText;
      modalDialogButton.onclick = function(){
        modalDialogButton.onclick = null;
        modalDialog.style.display = "none";
        if(callback){
          callback();
        }
      }
    }
    
    function hideMessage(){
      modalDialog.style.display = "none";
      modalDialogButton.onclick = null;
    }
      
    function sendAsync(url,payload, callback) {
      var request = new XMLHttpRequest();
      request.open('POST', url, true);
      request.setRequestHeader('Content-Type','application/json'); 

      request.onreadystatechange = function() {
        if (request.readyState === 4) {
          var result = request.responseText;
          var error = null;
          try {
            result = JSON.parse(result);
          } catch(e) {
            var message = !!result && !!result.error && !!result.error.message ? result.error.message : 'Invalid JSON RPC response: ' + JSON.stringify(result);
            error = {message:message,type:"JsonParse"};
          }
          callback(error, result);
        }
      };
      
      try {
        request.send(JSON.stringify(payload));
      } catch(e) {
        callback({message:'CONNECTION ERROR: Couldn\'t connect to node '+ url +'.',type:"noConnection"});
      }
    }
    
    function addBlocky(message, address){
      var icon = blockies.create({ 
        seed: address,
        size: 8,
        scale: 6
      });
      message.appendChild(icon);
    }
    
    function askAuthorization(transactionInfo, data, requireUnlock, sourceWindow){
      
        
      var value = transactionInfo["value"] ? transactionInfo.value : "0";
      var gasProvided = transactionInfo.gas;
      var gasPriceProvided = transactionInfo.gasPrice;
      var gasPrice = new BigNumber(gasPriceProvided,16); 
      var gas = new BigNumber(gasProvided,16);
      var weiValue = new BigNumber(value,16);
      var gasWeiValue = gas.times(gasPrice);
      var etherValue = weiValue.dividedBy(new BigNumber("1000000000000000000"));
      var gasEtherValue = gasWeiValue.dividedBy(new BigNumber("1000000000000000000"));
      
      hideWaiting();
      
      message.innerHTML = "";
      
      addBlocky(message,transactionInfo.from);
      
      var span = document.createElement('span');
      span.style="font-size:3em;";
      span.innerHTML = "&nbsp;&nbsp;&nbsp;" + "&#x2192;" + "&nbsp;&nbsp;&nbsp;";
      message.appendChild(span);
      
      addBlocky(message,transactionInfo.to);
      
      message.appendChild(document.createElement('br'));
      var textSpan = document.createElement("span");
      message.appendChild(textSpan);
      textSpan.innerHTML = etherValue.toFormat() + " ether <br/>  + gas cost (" + gasEtherValue.toFormat() + " ether )"
      
      if(requireUnlock){
        passwordField.style.display = "block"; 
      }else{
        passwordField.style.display = "none"; 
      }
      
      cancelButton.onclick = function(){
        sourceWindow.postMessage({id:data.id,result:null,error:{message:"Not Authorized"},type:"cancel"},firstUrl);
        closeWindow();
      }
      
      var submitFunc = function(){
        window.onbeforeunload = function (event) {
          if(!closedByCode){
            return "do not close now as a transaction is progress, this cannot be canceled and we wait for an answer";
          }
        };
        if(requireUnlock){
          if(password.value == ""){
            password.style.border = "2px solid red";
            return false;
          }
          password.style.border = "none";
          var params = [transactionInfo.from,password.value,3];
          showWaiting("Please wait...<br/>Do not close the window.");
          sendAsync(data.url,{id:999992,method:"personal_unlockAccount",params:params},function(error,result){
            if(error || result.error){
              showMessage("Error unlocking account", "Please retry.", hideWaiting);
            }else{
              sendAsync(data.url,data.payload,function(error,result){
                sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
                closeWindow();
              });
            }
          });
        }else{
          sendAsync(data.url,data.payload,function(error,result){
            if(result && result.error){
              processMessage(data,sourceWindow);
            }else{
              sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
              closeWindow();
            }
          });
          showWaiting();
        }
        return false;
      }
      
      form.onsubmit = submitFunc;
      confirmButton.onclick = submitFunc;
    }
    
    function needToAndCanUnlockAccount(address,url,callback){
      sendAsync(url,{id:9999990,method:"eth_sign",params:[address,"0xc6888fa8d57087278718986382264244252f8d57087278718986382264244252f"]},function(error,result){
        if(error || result.error){
          sendAsync(url,{id:9999991,method:"personal_listAccounts",params:[]},function(error,result){
            if(error || result.error){
              callback(true,false);
            }else{
              callback(true,true);
            }
          });
        }else{
          callback(false);
        }
      });
    }
      
    function receiveMessage(event){
      if(event.source != source){
        return;
      }
      if(firstUrl){
        if(firstUrl != event.origin){
          return;
        }
      }else{
        firstUrl = event.origin;
      }
      hideMessage();
      noMessageReceivedYet = false;
      var data = event.data;
      try{
        processMessage(data,event.source);
      }catch(e){
        event.source.postMessage({id:data.id,result:null,error:{message:"Could not process message data"},type:"notValid"},firstUrl);
        showMessage("Error","The application has sent invalid data", function(){
          closeWindow();
        });
      }
      
    }
    
    var allowedMethods = [
       "web3_clientVersion"
      ,"web3_sha3"
      ,"net_version"
      ,"net_peerCount"
      ,"net_listening"
      ,"eth_protocolVersion"
      ,"eth_syncing"
      ,"eth_coinbase"
      ,"eth_mining"
      ,"eth_hashrate"
      ,"eth_gasPrice"
      ,"eth_accounts"
      ,"eth_blockNumber"
      ,"eth_getBalance"
      ,"eth_getStorageAt"
      ,"eth_getTransactionCount"
      ,"eth_getBlockTransactionCountByHash"
      ,"eth_getBlockTransactionCountByNumber"
      ,"eth_getUncleCountByBlockHash"
      ,"eth_getUncleCountByBlockNumber"
      ,"eth_getCode"
      ,"eth_sendRawTransaction"
      ,"eth_call"
      ,"eth_estimateGas"
      ,"eth_getBlockByHash"
      ,"eth_getBlockByNumber"
      ,"eth_getTransactionByHash"
      ,"eth_getTransactionByBlockHashAndIndex"
      ,"eth_getTransactionByBlockNumberAndIndex"
      ,"eth_getTransactionReceipt"
      ,"eth_getUncleByBlockHashAndIndex"
      ,"eth_getUncleByBlockNumberAndIndex"
      ,"eth_getCompilers"
      ,"eth_compileLLL"
      ,"eth_compileSolidity"
      ,"eth_compileSerpent"
      ,"eth_newFilter"
      ,"eth_newBlockFilter"
      ,"eth_newPendingTransactionFilter"
      ,"eth_uninstallFilter"
      ,"eth_getFilterChanges"
      ,"eth_getFilterLogs"
      ,"eth_getLogs"
      ,"eth_getWork"
      ,"eth_submitWork"
      ,"eth_submitHashrate"
      // ,"shh_post"
      // ,"shh_version"
      // ,"shh_newIdentity"
      // ,"shh_hasIdentity"
      // ,"shh_newGroup"
      // ,"shh_addToGroup"
      // ,"shh_newFilter"
      // ,"shh_uninstallFilter"
      // ,"shh_getFilterChanges"
      // ,"shh_getMessages"
    ];
    
    function isMethodAllowed(method){
      return allowedMethods.indexOf(method) != -1;
    }
    
    function processMessage(data, sourceWindow){
      
      if(inIframe){
        if(isMethodAllowed(data.payload.method)){
          sendAsync(data.url,data.payload,function(error,result){
            sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
          });
        }else{
          sourceWindow.postMessage({id:data.id,result:null,error:{message:"method (" + data.payload.method + ") not allowed in iframe"},type:"notAllowed"},firstUrl);
        }
      }else if(data.payload.method == "eth_sendTransaction"){
        var transactionInfo = null;
        if(data.payload.params.length > 0){ 
          if(data.payload.params[0]["gas"] && data.payload.params[0]["gasPrice"] && data.payload.params[0]["to"] && data.payload.params[0]["from"]){
            transactionInfo = data.payload.params[0];
          }
        }
        if(transactionInfo != null){
          needToAndCanUnlockAccount(transactionInfo.from,data.url,function(requireUnlock,canUnlock){
            if(requireUnlock && canUnlock){
              askAuthorization(transactionInfo,data,true, sourceWindow);
            }else if(!requireUnlock){
              askAuthorization(transactionInfo,data,false,sourceWindow);
            }else if(requireUnlock && !canUnlock){
              var messageHtml = document.createElement('span');
              addBlocky(messageHtml,transactionInfo.from); 
              messageHtml.appendChild(document.createElement('br'));
              var span = document.createElement('span');
              span.innerHTML = "You need to unlock your account first : <br/>" + transactionInfo.from;
              messageHtml.appendChild(span);
              
              showMessage("Account Locked",messageHtml,function(){
                processMessage(data,sourceWindow);
              }, "Done");
            }
            
          });
        }else{
          sourceWindow.postMessage({id:data.id,result:null,error:{message:"Need to specify from , to, gas and gasPrice"},type:"notValid"},firstUrl);
          closeWindow();
        }
      }else{
        sourceWindow.postMessage({id:data.id,result:null,error:{message:"method (" + data.payload.method + ") not allowed in popup"},type:"notAllowed"},firstUrl);
      }     
    }
    
    function checkMessageNotReceived(){
      if(noMessageReceivedYet){
        showMessage("Error","No transaction received. Please make sure popup are not blocked.", function(){
          closeWindow();
        });
      }
    }
    setTimeout(checkMessageNotReceived,1000);
    
    window.addEventListener("message", receiveMessage);
    if(source){
      source.postMessage("ready","*");
    }
    
    </script>
  </body>
</html>
```


#eip-137.md
<pre>
  EIP: 137
  Title: Ethereum Domain Name Service - Specification
  Author: Nick Johnson <arachnid@notdot.net>
  Status: Final
  Type: Standards Track
  Category: ERC
  Created: 2016-04-04
</pre>

# Abstract

This draft EIP describes the details of the Ethereum Name Service, a proposed protocol and ABI definition that provides flexible resolution of short, human-readable names to service and resource identifiers. This permits users and developers to refer to human-readable and easy to remember names, and permits those names to be updated as necessary when the underlying resource (contract, content-addressed data, etc) changes. 

The goal of domain names is to provide stable, human-readable identifiers that can be used to specify network resources. In this way, users can enter a memorable string, such as 'vitalik.wallet' or 'www.mysite.swarm', and be directed to the appropriate resource. The mapping between names and resources may change over time, so a user may change wallets, a website may change hosts, or a swarm document may be updated to a new version, without the domain name changing. Further, a domain need not specify a single resource; different record types allow the same domain to reference different resources. For instance, a browser may resolve 'mysite.swarm' to the IP address of its server by fetching its A (address) record, while a mail client may resolve the same address to a mail server by fetching its MX (mail exchanger) record.
# Motivation

Existing [specifications](https://github.com/ethereum/wiki/wiki/Registrar-ABI) and [implementations](https://ethereum.gitbooks.io/frontier-guide/content/registrar_services.html) for name resolution in Ethereum provide basic functionality, but suffer several shortcomings that will significantly limit their long-term usefulness:
- A single global namespace for all names with a single 'centralised' resolver.
- Limited or no support for delegation and sub-names/sub-domains.
- Only one record type, and no support for associating multiple copies of a record with a domain.
- Due to a single global implementation, no support for multiple different name allocation systems.
- Conflation of responsibilities: Name resolution, registration, and whois information.

Use-cases that these features would permit include:
- Support for subnames/sub-domains - eg, live.mysite.tld and forum.mysite.tld.
- Multiple services under a single name, such as a DApp hosted in Swarm, a Whisper address, and a mail server.
- Support for DNS record types, allowing blockchain hosting of 'legacy' names. This would permit an Ethereum client such as Mist to resolve the address of a traditional website, or the mail server for an email address, from a blockchain name.
- DNS gateways, exposing ENS domains via the Domain Name Service, providing easier means for legacy clients to resolve and connect to blockchain services.

The first two use-cases, in particular, can be observed everywhere on the present-day internet under DNS, and we believe them to be fundamental features of a name service that will continue to be useful as the Ethereum platform develops and matures.

The normative parts of this document does not specify an implementation of the proposed system; its purpose is to document a protocol that different resolver implementations can adhere to in order to facilitate consistent name resolution. An appendix provides sample implementations of resolver contracts and libraries, which should be treated as illustrative examples only.

Likewise, this document does not attempt to specify how domains should be registered or updated, or how systems can find the owner responsible for a given domain. Registration is the responsibility of registrars, and is a governance matter that will necessarily vary between top-level domains.

Updating of domain records can also be handled separately from resolution. Some systems, such as swarm, may require a well defined interface for updating domains, in which event we anticipate the development of a standard for this.
# Specification
## Overview

The ENS system comprises three main parts:
- The ENS registry
- Resolvers
- Registrars

The registry is a single contract that provides a mapping from any registered name to the resolver responsible for it, and permits the owner of a name to set the resolver address, and to create subdomains, potentially with different owners to the parent domain.

Resolvers are responsible for performing resource lookups for a name - for instance, returning a contract address, a content hash, or IP address(es) as appropriate. The resolver specification, defined here and extended in other EIPs, defines what methods a resolver may implement to support resolving different types of records.

Registrars are responsible for allocating domain names to users of the system, and are the only entities capable of updating the ENS; the owner of a node in the ENS registry is its registrar. Registrars may be contracts or externally owned accounts, though it is expected that the root and top-level registrars, at a minimum, will be implemented as contracts.

Resolving a name in ENS is a two-step process. First, the ENS registry is called with the name to resolve, after hashing it using the procedure described below. If the record exists, the registry returns the address of its resolver. Then, the resolver is called, using the method appropriate to the resource being requested. The resolver then returns the desired result.

For example, suppose you wish to find the address of the token contract associated with 'beercoin.eth'. First, get the resolver:

```
var node = namehash("beercoin.eth");
var resolver = ens.resolver(node);
```

Then, ask the resolver for the address for the contract:

```
var hash = resolver.addr(node);
```

Because the `namehash` procedure depends only on the name itself, this can be precomputed and inserted into a contract, removing the need for string manipulation, and permitting O(1) lookup of ENS records regardless of the number of components in the raw name.
## Name Syntax

ENS names must conform to the following syntax:

<pre>&lt;domain> ::= &lt;label> | &lt;domain> "." &lt;label>
&lt;label> ::= any valid string label per [UTS46](http://unicode.org/reports/tr46/)
</pre>

In short, names consist of a series of dot-separated labels. Each label must be a valid normalised label as described in [UTS46](http://unicode.org/reports/tr46/) with the options `transitional=false` and `useSTD3AsciiRules=true`. For Javascript implementations, a [library](https://www.npmjs.com/package/idna-uts46) is available that normalises and checks names.

Note that while upper and lower case letters are allowed in names, the UTS46 normalisation process case-folds labels before hashing them, so two names with different case but identical spelling will produce the same namehash.

Labels and domains may be of any length, but for compatibility with legacy DNS, it is recommended that labels be restricted to no more than 64 characters each, and complete ENS names to no more than 255 characters. For the same reason, it is recommended that labels do not start or end with hyphens, or start with digits.

## namehash algorithm

Before being used in ENS, names are hashed using the 'namehash' algorithm. This algorithm recursively hashes components of the name, producing a unique, fixed-length string for any valid input domain. The output of namehash is referred to as a 'node'.

Pseudocode for the namehash algorithm is as follows:

```
def namehash(name):
  if name == '':
    return '\0' * 32
  else:
    label, _, remainder = name.partition('.')
    return sha3(namehash(remainder) + sha3(label))
```

Informally, the name is split into labels, each label is hashed. Then, starting with the last component, the previous output is concatenated with the label hash and hashed again. The first component is concatenated with 32 '0' bytes. Thus, 'mysite.swarm' is processed as follows:

```
node = '\0' * 32
node = sha3(node + sha3('swarm'))
node = sha3(node + sha3('mysite'))
```

Implementations should conform to the following test vectors for namehash:

    namehash('') = 0x0000000000000000000000000000000000000000000000000000000000000000
    namehash('eth') = 0x93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae
    namehash('foo.eth') = 0xde9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f

## Registry specification

The ENS registry contract exposes the following functions:

```
function owner(bytes32 node) constant returns (address);
```

Returns the owner (registrar) of the specified node.

```
function resolver(bytes32 node) constant returns (address);
```

Returns the resolver for the specified node.

```
function ttl(bytes32 node) constant returns (uint64);
```

Returns the time-to-live (TTL) of the node; that is, the maximum duration for which a node's information may be cached.

```
function setOwner(bytes32 node, address owner);
```

Transfers ownership of a node to another registrar. This function may only be called by the current owner of `node`. A successful call to this function logs the event `Transfer(bytes32 indexed, address)`.

```
function setSubnodeOwner(bytes32 node, bytes32 label, address owner);
```

Creates a new node, `sha3(node, label)` and sets its owner to `owner`, or updates the node with a new owner if it already exists. This function may only be called by the current owner of `node`. A successful call to this function logs the event `NewOwner(bytes32 indexed, bytes32 indexed, address)`.

```
function setResolver(bytes32 node, address resolver);
```

Sets the resolver address for `node`. This function may only be called by the owner of `node`. A successful call to this function logs the event `NewResolver(bytes32 indexed, address)`.

```
function setTTL(bytes32 node, uint64 ttl);
```

Sets the TTL for a node. A node's TTL applies to the 'owner' and 'resolver' records in the registry, as well as to any information returned by the associated resolver.
## Resolver specification

Resolvers may implement any subset of the record types specified here. Where a record types specification requires a resolver to provide multiple functions, the resolver MUST implement either all or none of them. Resolvers MUST specify a fallback function that throws.

Resolvers have one mandatory function:

```
function supportsInterface(bytes4 interfaceID) constant returns (bool)
```

The `supportsInterface` function is documented in [EIP 165](https://github.com/ethereum/EIPs/issues/165), and returns true if the resolver implements the interface specified by the provided 4 byte identifier. An interface identifier consists of the XOR of the function signature hashes of the functions provided by that interface; in the degenerate case of single-function interfaces, it is simply equal to the signature hash of that function. If a resolver returns `true` for `supportsInterface()`, it must implement the functions specified in that interface.

`supportsInterface` must always return true for `0x01ffc9a7`, which is the interface ID of `supportsInterface` itself.

 Currently standardised resolver interfaces are specified in the table below.

The following interfaces are defined:

| Interface name | Interface hash | Specification |
| --- | --- | --- |
| `addr` | 0x3b3b57de | [Contract address](#addr) |
| `name`      | 0x691f3431   | #181    |
| `ABI`       | 0x2203ab56   | #205    |
| `pubkey`    | 0xc8690233   | #619    |

EIPs may define new interfaces to be added to this registry.

### <a name="addr"></a>Contract Address Interface

Resolvers wishing to support contract address resources must provide the following function:

```
function addr(bytes32 node) constant returns (address);
```

If the resolver supports `addr` lookups but the requested node does not have a record, the resolver MUST return the zero address.

Clients resolving the `addr` record MUST check for a zero return value, and treat this in the same manner as a name that does not have a resolver specified - that is, refuse to send funds to or interact with the address. Failure to do this can result in users accidentally sending funds to the 0 address.

Changes to an address MUST trigger the following event:

```
event AddrChanged(bytes32 indexed node, address a);
```
# Appendix A: Registry Implementation

```
contract ENS {
    struct Record {
        address owner;
        address resolver;
        uint64 ttl;
    }

    mapping(bytes32=>Record) records;

    event NewOwner(bytes32 indexed node, bytes32 indexed label, address owner);
    event Transfer(bytes32 indexed node, address owner);
    event NewResolver(bytes32 indexed node, address resolver);

    modifier only_owner(bytes32 node) {
        if(records[node].owner != msg.sender) throw;
        _
    }

    function ENS(address owner) {
        records[0].owner = owner;
    }

    function owner(bytes32 node) constant returns (address) {
        return records[node].owner;
    }

    function resolver(bytes32 node) constant returns (address) {
        return records[node].resolver;
    }

    function ttl(bytes32 node) constant returns (uint64) {
        return records[node].ttl;
    }

    function setOwner(bytes32 node, address owner) only_owner(node) {
        Transfer(node, owner);
        records[node].owner = owner;
    }

    function setSubnodeOwner(bytes32 node, bytes32 label, address owner) only_owner(node) {
        var subnode = sha3(node, label);
        NewOwner(node, label, owner);
        records[subnode].owner = owner;
    }

    function setResolver(bytes32 node, address resolver) only_owner(node) {
        NewResolver(node, resolver);
        records[node].resolver = resolver;
    }

    function setTTL(bytes32 node, uint64 ttl) only_owner(node) {
        NewTTL(node, ttl);
        records[node].ttl = ttl;
    }
}
```
# Appendix B: Sample Resolver Implementations
### Built-in resolver

The simplest possible resolver is a contract that acts as its own name resolver by implementing the contract address resource profile:

```
contract DoSomethingUseful {
    // Other code

    function addr(bytes32 node) constant returns (address) {
        return this;
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```

Such a contract can be inserted directly into the ENS registry, eliminating the need for a separate resolver contract in simple use-cases. However, the requirement to 'throw' on unknown function calls may interfere with normal operation of some types of contract.

### Standalone resolver

A basic resolver that implements the contract address profile, and allows only its owner to update records:

```
contract Resolver {
    event AddrChanged(bytes32 indexed node, address a);

    address owner;
    mapping(bytes32=>address) addresses;

    modifier only_owner() {
        if(msg.sender != owner) throw;
        _
    }

    function Resolver() {
        owner = msg.sender;
    }

    function addr(bytes32 node) constant returns(address) {
        return addresses[node];    
    }

    function setAddr(bytes32 node, address addr) only_owner {
        addresses[node] = addr;
        AddrChanged(node, addr);
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```

After deploying this contract, use it by updating the ENS registry to reference this contract for a name, then calling `setAddr()` with the same node to set the contract address it will resolve to.
### Public resolver

Similar to the resolver above, this contract only supports the contract address profile, but uses the ENS registry to determine who should be allowed to update entries:

```
contract PublicResolver {
    event AddrChanged(bytes32 indexed node, address a);
    event ContentChanged(bytes32 indexed node, bytes32 hash);

    ENS ens;
    mapping(bytes32=>address) addresses;

    modifier only_owner(bytes32 node) {
        if(ens.owner(node) != msg.sender) throw;
        _
    }

    function PublicResolver(address ensAddr) {
        ens = ENS(ensAddr);
    }

    function addr(bytes32 node) constant returns (address ret) {
        ret = addresses[node];
    }

    function setAddr(bytes32 node, address addr) only_owner(node) {
        addresses[node] = addr;
        AddrChanged(node, addr);
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```
# Appendix C: Sample Registrar Implementation

This registrar allows users to register names at no cost if they are the first to request them.

```
contract FIFSRegistrar {
    ENS ens;
    bytes32 rootNode;

    function FIFSRegistrar(address ensAddr, bytes32 node) {
        ens = ENS(ensAddr);
        rootNode = node;
    }

    function register(bytes32 subnode, address owner) {
        var node = sha3(rootNode, subnode);
        var currentOwner = ens.owner(node);
        if(currentOwner != 0 && currentOwner != msg.sender)
            throw;

        ens.setSubnodeOwner(rootNode, subnode, owner);
    }
}
```


#eip-141.md
## Preamble

    EIP: 141
    Title: Designated invalid EVM instruction
    Author: Alex Beregszaszi
    Type: Standard Track
    Category: Core
    Status: Accepted
    Created: 2017-02-09

## Abstract

An instruction is designated to remain as an invalid instruction.

## Motivation

The invalid instruction can be used as a distinct reason to abort execution.

## Specification

The opcode `0xfe` is the `INVALID` instruction. It can be used to abort the execution (i.e. duplicates as an `ABORT` instruction).

## Backwards Compatibility

This instruction was never used and therefore has no effect on past contracts.

## Copyright

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).


#eip-150.md
## Preamble
```
EIP: 150
Title: Gas cost changes for IO-heavy operations
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-09-24
```

### Specification

If `block.number >= FORK_BLKNUM`, then:
- Increase the gas cost of EXTCODESIZE to 700
- Increase the base gas cost of EXTCODECOPY to 700
- Increase the gas cost of BALANCE to 400
- Increase the gas cost of SLOAD to 200
- Increase the gas cost of CALL, DELEGATECALL, CALLCODE to 700
- Increase the gas cost of SELFDESTRUCT to 5000
- If SELFDESTRUCT hits a newly created account, it triggers an additional gas cost of 25000 (similar to CALLs)
- Increase the recommended gas limit target to 5.5 million
- Define "all but one 64th" of `N` as `N - floor(N / 64)`
- If a call asks for more gas than the maximum allowed amount (ie. total amount of gas remaining in the parent after subtracting the gas cost of the call and memory expansion), do not return an OOG error; instead, if a call asks for more gas than all but one 64th of the maximum allowed amount, call with all but one 64th of the maximum allowed amount of gas (this is equivalent to a version of #90 plus #114). CREATE only provides all but one 64th of the parent gas to the child call.

That is, substitute:

```
        extra_gas = (not ext.account_exists(to)) * opcodes.GCALLNEWACCOUNT + \
            (value > 0) * opcodes.GCALLVALUETRANSFER
        if compustate.gas < gas + extra_gas:
            return vm_exception('OUT OF GAS', needed=gas+extra_gas)
        submsg_gas = gas + opcodes.GSTIPEND * (value > 0)
```

With:

```
        def max_call_gas(gas):
          return gas - (gas // 64)

        extra_gas = (not ext.account_exists(to)) * opcodes.GCALLNEWACCOUNT + \
            (value > 0) * opcodes.GCALLVALUETRANSFER
        if compustate.gas < extra_gas:
            return vm_exception('OUT OF GAS', needed=extra_gas)
        if compustate.gas < gas + extra_gas:
            gas = min(gas, max_call_gas(compustate.gas - extra_gas))
        submsg_gas = gas + opcodes.GSTIPEND * (value > 0)
```

### Rationale

Recent denial-of-service attacks have shown that opcodes that read the state tree are under-priced relative to other opcodes. There are software changes that have been made, are being made and can be made in order to mitigate the situation; however, the fact will remain that such opcodes will be by a substantial margin the easiest known mechanism to degrade network performance via transaction spam. The concern arises because it takes a long time to read from disk, and is additionally a risk to future sharding proposals as the "attack transactions" that have so far been most successful in degrading network performance would also require tens of megabytes to provide Merkle proofs for. This EIP increases the cost of storage reading opcodes to address this concern. The costs have been derived from an updated version of the calculation table used to generate the 1.0 gas costs: https://docs.google.com/spreadsheets/d/15wghZr-Z6sRSMdmRmhls9dVXTOpxKy8Y64oy9MvDZEQ/edit#gid=0 ; the rules attempt to target a limit of 8 MB of data that needs to be read in order to process a block, and include an estimate of 500 bytes for a Merkle proof for SLOAD and 1000 for an account.

This EIP aims to be simple, and adds a flat penalty of 300 gas on top of the costs calculated in this table to account for the cost of loading the code (~17-21 kb in the worst case).

The EIP 90 gas mechanic is introduced because without it, all current contracts that make calls would stop working as they use an expression like `msg.gas - 40` to determine how much gas to make a call with, relying on the gas cost of calls being 40. Additionally, EIP 114 is introduced because, given that we are making the cost of a call higher and less predictable, we have an opportunity to do it at no extra cost to currently available guarantees, and so we also achieve the benefit of replacing the call stack depth limit with a "softer" gas-based restriction, thereby eliminating call stack depth attacks as a class of attack that contract developers have to worry about and hence increasing contract programming safety. Note that with the given parameters, the de-facto maximum call stack depth is limited to ~340 (down from ~1024), mitigating the harm caused by any further potential quadratic-complexity DoS attacks that rely on calls.

The gas limit increase is recommended so as to preserve the de-facto transactions-per-second processing capability of the system for average contracts.


#eip-155.md
## Preamble
```
EIP: 155
Title: Simple replay attack protection
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-10-14
```

### Parameters
- `FORK_BLKNUM`: TBA
- `CHAIN_ID`: 1
### Specification

If `block.number >= FORK_BLKNUM` and `v = CHAIN_ID * 2 + 35` or `v = CHAIN_ID * 2 + 36`, then when computing the hash of a transaction for purposes of signing or recovering, instead of hashing only the first six elements (ie. nonce, gasprice, startgas, to, value, data), hash nine elements, with `v` replaced by `CHAIN_ID`, `r = 0` and `s = 0`. The currently existing signature scheme using `v = 27` and `v = 28` remains valid and continues to operate under the same rules as it does now.
### Example

Consider a transaction with `nonce = 9`, `gasprice = 20 * 10**9`, `startgas = 21000`, `to = 0x3535353535353535353535353535353535353535`, `value = 10**18`, `data=''` (empty).

The "signing data" becomes:

```
0xec098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a764000080018080
```

The "signing hash" becomes:

```
0xdaf5a779ae972f972197303d7b574746c7ef83eadac0f2791ad23db92e4c8e53
```

If the transaction is signed with the private key `0x4646464646464646464646464646464646464646464646464646464646464646`, then the v,r,s values become:

```
(37, 18515461264373351373200002665853028612451056578545711640558177340181847433846, 46948507304638947509940763649030358759909902576025900602547168820602576006531)
```

Notice the use of 37 instead of 27. The signed tx would become:

```
0xf86c098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a76400008025a028ef61340bd939bc2195fe537567866003e1a15d3c71ff63e1590620aa636276a067cbe9d8997f761aecb703304b3800ccf555c9f3dc64214b297fb1966a3b6d83
```
### Rationale

This would provide a way to send transactions that work on ethereum without working on ETC or the Morden testnet. ETC is encouraged to adopt this EIP but replacing `CHAIN_ID` with a different value, and all future testnets, consortium chains and alt-etherea are encouraged to adopt this EIP replacing `CHAIN_ID` with a unique value.


### List of Chain ID's:

| `CHAIN_ID`     | Chain(s)                                   |
| ---------------| -------------------------------------------|
| 1              | Ethereum mainnet                           |
| 2              | Morden (disused), Expanse mainnet          |
| 3              | Ropsten                                    |
| 4              | Rinkeby                                    |
| 30             | Rootstock mainnet                          |
| 31             | Rootstock testnet                          |
| 42             | Kovan                                      |
| 61             | Ethereum Classic mainnet                   |
| 62             | Ethereum Classic testnet                   |
| 1337           | Geth private chains (default)              |


#eip-158.md
```
EIP: 158
Title: State clearing
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Superseded
Created: 2016-10-16
Superseded-By: 161
```

# Specification

For all blocks where `block.number >= FORK_BLKNUM` (TBA):
1. In all cases where a state change is made to an account, and this state change results in the account state being saved with nonce = 0, balance = 0, code empty, storage empty (hereinafter "empty account"), the account is instead deleted.
2. If a address is "touched" and that address contains an empty account, then it is deleted. A "touch" is defined as any situation where if the account at the given address were nonexistent it would be created.
3. Whenever the EVM checks if an account exists, emptiness is treated as equivalent to nonexistence. Particularly, note that this implies that, once this change is enabled, there is no longer a meaningful difference between emptiness and nonexistence from the point of view of EVM execution.
4. Zero-value calls and zero-value suicides no longer consume the 25000 account creation gas cost in any circumstance

The cases where a "touch" takes place can be enumerated as follows:
- Zero-value-bearing CALLs
- CREATEs (if the code that is ultimately saved is empty and there is no ether remaining in the account when it is saved)
- Zero-value-bearing SUICIDEs
- Transaction recipients
- Contracts created in contract creation transactions
- Miners receiving transaction fees (note the case where the gasprice is zero, and the account does not yet exist because it only receives the block/uncle/nephew rewards _after_ processing every transaction)
### Specification (1b)

When the EVM checks for emptiness (for the purpose of possibly applying the 25000 gas cost), emptiness is defined by `is_empty(acct): return get_balance(acct) == 0 and get_code(acct) == "" and get_nonce(acct) == 0`; emptiness of storage does not matter. This simplifies client implementation because there is no need to add extra complexity to make caches enumerable in the correct way and does not significantly affect the intended result, as the cases where balance/code/nonce are empty but storage is nonempty where this change would lead to an extra 25000 gas being paid are pathological and have no real use value.
### Specification (1c)

Do not implement point 2 above (ie. no new empty accounts can be created, but existing ones are not automatically destroyed unless their state is actually _changed_). Instead, during each block starting from (and including) N and ending when there are no null accounts left, select the 1000 null accounts that are left-most in order of sha3(address), and delete them (ordering by hash is necessary so as to allow the accounts to be easily found by iterating the tree).
# Rationale

This removes a large number of empty accounts that have been put in the state at very low cost due to flaws in earlier versions of the Ethereum protocol, thereby greatly reducing state size and hence both reducing the hard disk load of a full client and reducing the time for a fast sync. Additionally, it simplifies the protocol in the long term, as once all "empty" objects are cleared out there is no longer any meaningful distinction between an account being empty and being nonexistent, and indeed one can simply view nonexistence as a compact representation of emptiness.

Note that this proposal does introduce a **temporary** breaking of existing guarantees, in that by repeatedly zero-value-calling already existing empty accounts one can create a state change at a cost of 700 gas per account instead of the usual 5000 per gas minimum (with SUICIDE refunds this goes down further to 350 gas per account). Allowing such a large number of state writes per block will lead to heightened block processing times and increase uncle rates in the short term while the existing empty accounts are being cleared, and eventually once all empty accounts are cleared this issue will no longer exist.

# References

1. EIP-158 issue and discussion: https://github.com/ethereum/EIPs/issues/158
2. EIP-161 issue and discussion: https://github.com/ethereum/EIPs/issues/161


#eip-161.md
```
EIP: 161
Title: State trie clearing (invariant-preserving alternative)
Author: Gavin Wood
Type: Standard Track
Category: Core
Status: Final
Created: 2016-10-24
```

# Specification

a. Account creation transactions and the `CREATE` operation SHALL, prior to the execution of the initialisation code, **increment** the **nonce** over and above its normal starting value by **one** (for normal networks, this will be simply 1, however test-nets with non-zero default starting nonces will be different).

b. Whereas `CALL` and `SUICIDE` would charge 25,000 gas when the destination is non-existent, now the charge SHALL **only** be levied if the operation transfers **more than zero value** and the destination account is _dead_.

c. No account may _change state_ from non-existent to existent-but-_empty_. If an operation would do this, the account SHALL instead remain non-existent.

d. _At the end of the transaction_, any account _touched_ by the execution of that transaction which is now _empty_ SHALL instead become non-existent (i.e. **deleted**).

Where:

An account is considered to be _touched_ when it is involved in any potentially _state-changing_ operation. This includes, but is not limited to, being the recipient of a **transfer of zero value**.

An account is considered _empty_ when it has **no code** and **zero nonce** and **zero balance**.

An account is considered _dead_ when either it is non-existent or it is _empty_.

_At the end of the transaction_ is immediately following the execution of the suicide list, prior to the determination of the state trie root for receipt population.

An account _changes state_ when:
- it is the target or refund of a `SUICIDE` operation for **zero or more** value;
- it is the source or destination of a `CALL` operation or message-call transaction transferring **zero or more** value;
- it is the source or newly-creation of a `CREATE` operation or contract-creation transaction endowing **zero or more** value;
- as the block author ("miner") it is recipient of block-rewards or transaction-fees of **zero or more**.

## Notes

In the present Ethereum protocol, it should be noted that very few state changes can ultimately result in accounts that are empty following the execution of the transaction. In fact there are only four contexts that current implementations need track:
- an empty account has zero value transferred to it through `CALL`;
- an empty account has zero value transferred to it through `SUICIDE`;
- an empty account has zero value transferred to it through a message-call transaction;
- an empty account has zero value transferred to it through a zero-gas-price fees transfer.

# Rationale

Same as #158 except that several edge cases are avoided since we do not break invariants:
- ~~that an account can go from having code and storage to not having code or storage mid-way through the execution of a transaction;~~ [corrected]
- that a newly created account cannot be deleted prior to being deployed.

`CREATE` avoids zero in the nonce to avoid any suggestion of the oddity of `CREATE`d accounts being reaped half-way through their creation.

# References

1. EIP-158 issue and discussion: https://github.com/ethereum/EIPs/issues/158
2. EIP-161 issue and discussion: https://github.com/ethereum/EIPs/issues/161


#eip-162.md
```
EIP: 162
Title: Initial ENS Hash Registrar
Author: Maurelian and Nick Johnson
Status: Final
Type: Informational
Created: 2016-10-25
```

## Contents
- Abstract
- Motivations
- Specification
  - Initial restrictions
  - Name format for hash registration
  - Auctioning names
  - Deeds
  - Deployment and Upgrade process
  - Registrar Interface
- Rationale
  - Not committing to a permanent registrar at the outset
  - Valid names >= 7 characters
  - Restricting TLD to `.eth`
  - Holding ether as collateral
- Prior work

<!-- /MarkdownTOC -->

## Abstract

This ERC describes the implementation, as deployed to the main ethereum network on 2017-05-04, of a registrar contract to govern the allocation of names in the Ethereum Name Service (ENS). The corresponding source code is [here](https://github.com/ethereum/ens/blob/mainnet/contracts/HashRegistrarSimplified.sol).

For more background, refer to [EIP 137](https://github.com/ethereum/EIPs/issues/137).

> Registrars are responsible for allocating domain names to users of the system, and are the only entities capable of updating the ENS; the owner of a node in the ENS registry is its registrar. Registrars may be contracts or externally owned accounts, though it is expected that the root and top-level registrars, at a minimum, will be implemented as contracts.
>
> \- EIP 137

A well designed and governed registrar is essential to the success of the ENS described in EIP 137, but is described separately in this document as it is external to the core ENS protocol.

In order to maximize utility and adoption of a new namespace, the registrar should mitigate speculation and "name squatting", however the best approach for mitigation is unclear. Thus an "initial" registrar is proposed, which implements a simple approach to name allocation. During the initial period, the available namespace will be significantly restricted to the `.eth` top level domain, and subdomain shorter than 7 characters in length disallowed. This specification largely describes @alexvandesande and @arachnid's [hash registrar implementation](https://github.com/Arachnid/ens/blob/master/HashRegistrarSimplified.sol) in order to facilitate discussion.

The intent is to replace the Initial Registrar contract with a permanent registrar contract. The Permanent Registrar will increase the available namespace, and incorporate lessons learned from the performance of the Initial Registrar. This upgrade is expected to take place within approximately 2 years of initial deployment.

## Motivations

The following factors should be considered in order to optimize for adoption of the ENS, and good governance of the Initial Registrar's namespace.

**Upgradability:** The Initial Registrar should be safely upgradeable, so that knowledge gained during its deployment can be used to replace it with an improved and permanent registrar.

**Effective allocation:** Newly released namespaces often create a land grab situation, resulting in many potentially valuable names being purchased but unused, with the hope of re-selling at a profit. This reduces the availability of the most useful names, in turn decreasing the utility of the name service to end users.

Achieving an effective allocation may or may not require human intervention for dispute resolution and other forms of curation. The Initial Registrar should not aim to create to most effective possible allocation, but instead limit the cost of misallocation in the long term.

**Security:** The registrar will hold a balance of ether without an explicit limit. It must be designed securely.

**Simplicity:** The ENS specification itself emphasizes a separation of concerns, allowing the most essential element, the registry to be as simple as possible. The interim registrar in turn should be as simple as possible while still meeting its other design goals.

**Adoption:** Successful standards become more successful due to network effects. The registrar should consider what strategies will encourage the adoption of the ENS in general, and the namespace it controls in particular.

## Specification

### Initial restrictions

The Initial Registrar is expected to be in service for approximately two years, prior to upgrading. This should be sufficient time to learn, observe, and design an updated system.

During the initial two year period, the available name space will be restricted to the `.eth` TLD.

This restriction is enforced by the owner of the ENS root node who should not assign any nodes other than `.eth` to the Initial Registrar. The ENS's root node should be controlled by multiple parties using a multisig contract.

The Initial Registrar will also prohibit registration of names 6 characters or less in length.

### Name format for hash registration

Names submitted to the initial registrar must be hashed using Ethereum's sha3 function. Note that the hashes submitted to the registrar are the hash of the subdomain label being registered, not the namehash as defined in EIP 137.

For example, in order to register `abcdefg.eth`, one should submit `sha3('abcdefg')`, not `sha3(sha3(0, 'eth'), 'abcdefg')`.

### Auctioning names

The registrar will allocate the available names through a Vickrey auction:

> A Vickrey auction is a type of sealed-bid auction. Bidders submit written bids without knowing the bid of the other people in the auction. The highest bidder wins but the price paid is the second-highest bid. This type of auction... gives bidders an incentive to bid their true value.
>
> \- [Vickrey Auction, Wikipedia](https://en.wikipedia.org/wiki/Vickrey_auction)

The auction lifecycle of a name has 5 possible states, or Modes.

1. **Not-yet-available:** The majority of names will be initially unavailable for auction, and will become available some time during the 8 weeks after launch.
2. **Open:** The earliest availability for a name is determined by the most significant byte of its sha3 hash. `0x00` would become available immediately, `0xFF` would become available after 8 weeks, and the availability of other names is distributed accordingly. Once a name is available, it is possible to start an auction on it.
3. **Auction:** Once the auction for a name has begun, there is a 72 hour bidding period. Bidders must submit a payment of ether, along with sealed bids as a hash of `sha3(bytes32 hash, address owner, uint value, bytes32 salt)`. The bidder may obfuscate the true bid value by sending a greater amount of ether.
4. **Reveal:** After the bidding period, a 48 hour reveal period commences. During this time, bidders must reveal the true parameters of their sealed bid. As bids are revealed, ether payments are returned according to the schedule of "refund ratios" outlined in the table below. If no bids are revealed, the name will return to the Open state.
5. **Owned:** After the reveal period has finished, the winning bidder must submit a transaction to finalize the auction, which then calls the ENS's `setSubnodeOwner` function, recording the winning bidder's address as the owner of the hash of the name.

The following table outlines important parameters which define the Registrar's auction mechanism.

#### Registrar Parameters

|        Name        |                                            Description                                             |   Value    |
|--------------------|----------------------------------------------------------------------------------------------------|------------|
| totalAuctionLength | The full time period from start of auction to end of the reveal period.                            | 5 days     |
| revealPeriod       | The length of the time period during which bidding is no longer allowed, and bids must be revealed. | 48 hours   |
| launchLength       | The time period during which all names will become available for auction.                          | 8 weeks    |
| minPrice           | The minimum amount of ether which must be locked up in exchange for ownership of a name.           | 0.01 ether |

### Deeds

The Initial Registrar contract does not hold a balance itself. All ether sent to the Registrar will be held in a separate `Deed` contracts. A deed contract is first created and funded when a sealed bid is submitted. After an auction is completed and a hash is registered, the deed for the winning bid is held in exchange for ownership of the hash. Non-winning bids are refunded.

A deed for an owned name may be transferred to another account by its owner, thus transferring ownership and control of the name.

After 1 year of registration, the owner of a hash may choose to relinquish ownership and have the value of the deed returned to them.

Deeds for non-winning bids can be closed by various methods, at which time any ether held will either be returned to the bidder, burnt, or sent to someone else as a reward for actions which help the registrar.

The following table outlines what portion of the balance held in a deed contract will be returned upon closure, and to whom. The remaining balance will be burnt.

#### Refund schedule

| Reason for Deed closure | Refund Recipient | Refund Percentage |
| --- | --- | --- |
| A valid non-winning bid is revealed. | Bidder | 99.5% |
| A bid submitted after the auction period is revealed. | Bidder | 99.5% |
| A bid is revealed after the reveal period. <sup>1</sup> | Bidder | 0.5% |
| An expired sealed bid is cancelled. <sup>2</sup> | Canceler | 0.5% |
| A registered hash is reported as invalid. <sup>3</sup> | Reporter | 50% |
| A registered hash is reported as invalid. <sup>3</sup> | Owner | 50% |

##### Notes:

1. This incentivizes all bids to be revealed in time. If bids could be revealed late, an extortion attack on the current highest bidder could be made by threatening to reveal a new second highest bid.
2. A bid which remains sealed after more than 2 weeks and 5 days may be cancelled by anyone to collect a small reward.
2. Since names are hashed before auctioning and registration, the Initial Registrar is unable to enforce character length restrictions independently. A reward is therefore provided for reporting invalid names.

### Deployment and Upgrade process

The Initial Registrar requires the ENS's address as a contructor, and should be deployed after the ENS. The multisig account owning the root node in the ENS should then set the Initial Registrar's address as owner of the `eth` node.

The Initial Registrar is expected to be replaced by a Permanent Registrar approximately 2 years after deployment. The following process should be used for the upgrade:
1. The Permanent Registrar contract will be deployed.
2. The multisig account owning the root node in the ENS will assign ownership of the `.eth` node to the Permanent Registrar.
3. Owners of hashes in the Initial Registrar will be responsible for registering their deeds to the Permanent Registrar. A couple options are considered here:
   1. Require owners to transfer their ownership prior to a cutoff date in order to maintain ownership and/or continue name resolution services.
   2. Have the Permanent Registrar query the Initial Registrar for ownership if it is lacking an entry.

### Planned deactivation

In order to limit dependence on the Initial Registrar, new auctions will stop after 4 years, and all ether held in deeds after 8 years will become unreachable.

### Registrar Interface

`function state(bytes32 _hash) constant returns (Mode)`
- Implements a state machine returning the current state of a name

`function entries(bytes32 _hash) constant returns (Mode, address, uint, uint, uint)`
- Returns the following information regarding a registered name:
  * state
  * deed address
  * registration date
  * balance of the deed
  * highest value bid at auction

`function getAllowedTime(bytes32 _hash) constant returns (uint timestamp)`
- Returns the time at which the hash will no longer be in the initial `not-yet-available` state.

`function isAllowed(bytes32 _hash, uint _timestamp) constant returns (bool allowed)`
- Takes a hash and a time, returns true if and only if it has passed the initial `not-yet-available` state.

`function startAuction(bytes32 _hash);`
- Moves the state of a hash from Open to Auction. Throws if state is not Open.

`function startAuctions(bytes32[] _hashes);`
- Starts multiple auctions on an array of hashes. This enables someone to open up an auction for a number of dummy hashes when they are only really interested in bidding for one. This will increase the cost for an attacker to simply bid blindly on all new auctions. Dummy auctions that are open but not bid on are closed after a week.

`function shaBid(bytes32 hash, address owner, uint value, bytes32 salt) constant returns (bytes32 sealedBid);`
- Takes the parameters of a bid, and returns the sealedBid hash value required to participate in the bidding for an auction. This obfuscates the parameters in order to mimic the mechanics of placing a bid in an envelope.

`function newBid(bytes32 sealedBid);`
- Bids are sent by sending a message to the main contract with a sealedBid hash and an amount of ether. The hash contains information about the bid, including the bidded name hash, the bid value, and a random salt. Bids are not tied to any one auction until they are revealed. The value of the bid itself can be masqueraded by sending more than the value of your actual bid. This is followed by a 48h reveal period. Bids revealed after this period will be burned and the ether unrecoverable. Since this is an auction, it is expected that most public hashes, like known domains and common dictionary  words, will have multiple bidders pushing the price up.

`function startAuctionsAndBid(bytes32[] hashes, bytes32 sealedBid)`
- A utility function allowing a call to `startAuctions` followed by `newBid` in a single transaction.


`function unsealBid(bytes32 _hash, address _owner, uint _value, bytes32 _salt);`
- Once the bidding period is completed, there is a reveal period during with the properties of a bid are submitted to reveal them. The registrar hashes these properties using the `shaBid()` function above to verify that they match a pre-existing sealed bid. If the unsealedBid is the new best bid, the old best bid is returned to its bidder.

`function cancelBid(bytes32 seal);`
- Cancels an unrevealed bid according to the rules described in the notes on the refund schedule above.

`function finalizeAuction(bytes32 _hash);`

After the registration date has passed, this function can be called to finalize the auction, which then calls the ENS function `setSubnodeOwner()`  updating the ENS record to set the winning bidder as owner of the node.

`function transfer(bytes32 _hash, address newOwner);`
- Update the owner of the ENS node corresponding to the submitted hash to a new owner. This function must be callable only by the current owner.

`function releaseDeed(bytes32 _hash);`
- After some time, the owner can release the property and get their ether back.

`function invalidateName(string unhashedName);`
- Since registration is done on the hash of a name, the registrar itself cannot validate names. This function can be used to report a name which is 6 characters long or less. If it has been registered, the submitter will earn 10% of the deed value. We are purposefully handicapping the simplified registrar as a way to force it into being restructured in a few years.

`function eraseNode(bytes32[] labels)`
- Allows anyone to delete the owner and resolver records for a subdomain of a name that is not currently owned in the registrar. For instance, to zero `foo.bar.eth` on a registrar that owns `.eth`, pass an array containing `[sha3('foo'), sha3('bar')]`.

`function transferRegistrars(bytes32 _hash) onlyOwner(_hash);`
- Used during the upgrade process to a permanent registrar. If this registrar is no longer the owner of the its root node in the ENS, this function will transfers the deed to the current owner, which should be a new registrar. This function throws if this registrar still owns its root node.

## Rationale

### Starting with a temporary registrar

Anticipating and designing for all the potential issues of name allocation names is unlikely to succeed. This approach chooses not to be concerned with getting it perfect, but allows us to observe and learn with training wheels on, and implement improvements before expanding the available namespace to shorter names or another TLD.

### Valid names >= 7 characters

Preserving the shortest, and often most valuable, domain names for the upgraded registrar provides the opportunity to implement processes for dispute resolution (assuming they are found to be necessary).

### Delayed release of names

A slower release allows for extra time to identify, and address any issues which may arise after launch.

### Restricting TLD to `.eth`

Choosing a single TLD helps to maximize network effects by focusing on one namespace.

A three letter TLD is a pattern made familiar by it's common usage in internet domain names. This familiarity significantly increases the potential of the ENS to be integrated into pre-existing DNS systems, and reserved as a [special-use domain name](http://www.iana.org/assignments/special-use-domain-names/special-use-domain-names.xhtml#special-use-domain).  A recent precedent for this is the [reservation of the `.onion` domain](https://tools.ietf.org/html/rfc7686).

### Holding ether as collateral

This approach is simpler than the familiar model of requiring owners to make recurring payments to retain ownership of a domain name. It also makes the initial registrar a revenue neutral service.

## Prior work

This document borrows heavily from several sources:
- [EIP 137](https://github.com/ethereum/EIPs/issues/137) outlines the initial implementation of the Registry Contract (ENS.sol) and associated Resolver contracts.
- [ERC 26](https://github.com/ethereum/EIPs/issues/26) was the first ERC to propose a name service at the contract layer
- @alexvandesande's current implementation of the [HashRegistrar](https://github.com/Arachnid/ens/blob/master/HashRegistrarSimplified.sol)

### Edits:
- 2016-10-26 Added link Alex's design in abstract
- 2016-11-01 change 'Planned deactivation' to h3'
- 2017-03-13 Update timelines for bidding and reveal periods


#eip-170.md
```
EIP: 170
Title: Contract code size limit
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-11-04
```

### Specification

If `block.number >= FORK_BLKNUM`, then if contract creation initialization returns data with length of **more than** `0x6000` (`2**14 + 2**13`) bytes, contract creation fails with an out of gas error.

### Rationale

Currently, there remains one slight quadratic vulnerability in ethereum: when a contract is called, even though the call takes a constant amount of gas, the call can trigger O(n) cost in terms of reading the code from disk, preprocessing the code for VM execution, and also adding O(n) data to the Merkle proof for the block's proof-of-validity. At current gas levels, this is acceptable even if suboptimal. At the higher gas levels that could be triggered in the future, possibly very soon due to dynamic gas limit rules, this would become a greater concern - not nearly as serious as recent denial of service attacks, but still inconvenient especially for future light clients verifying proofs of validity or invalidity. The solution is to put a hard cap on the size of an object that can be saved to the blockchain, and do so non-disruptively by setting the cap at a value slightly higher than what is feasible with current gas limits.

### References

1. EIP-170 issue and discussion: https://github.com/ethereum/EIPs/issues/170
2. pyethereum implementation: https://github.com/ethereum/pyethereum/blob/5217294871283d8dc4fb3ca9d8a78c7d416490e8/ethereum/messages.py#L397


#eip-181.md
<pre>
  EIP: 181
  Title: ENS support for reverse resolution of Ethereum addresses
  Author: Nick Johnson <arachnid@notdot.net>
  Status: Final
  Type: Standard Track
  Category: ERC
  Created: 2016-12-01
</pre>

# Abstract
This EIP specifies a TLD, registrar, and resolver interface for reverse resolution of Ethereum addresses using ENS. This permits associating a human-readable name with any Ethereum blockchain address. Resolvers can be certain that the reverse record was published by the owner of the Ethereum address in question.

# Motivation
While name services are mostly used for forward resolution - going from human-readable identifiers to machine-readable ones - there are many use-cases in which reverse resolution is useful as well:

 - Applications that allow users to monitor accounts benefit from showing the name of an account instead of its address, even if it was originally added by address.
 - Attaching metadata such as descriptive information to an address allows retrieving this information regardless of how the address was originally discovered.
 - Anyone can configure a name to resolve to an address, regardless of ownership of that address. Reverse records allow the owner of an address to claim a name as authoritative for that address.

# Specification
Reverse ENS records are stored in the ENS hierarchy in the same fashion as regular records, under a reserved domain, `addr.reverse`. To generate the ENS name for a given account's reverse records, convert the account to hexadecimal representation in lower-case, and append `addr.reverse`. For instance, the ENS registry's address at `0x112234455c3a32fd11230c42e7bccd4a84e02010` has any reverse records stored at `112234455c3a32fd11230c42e7bccd4a84e02010.addr.reverse`.

Note that this means that contracts wanting to do dynamic reverse resolution of addresses will need to perform hex encoding in the contract.

## Registrar
The owner of the `addr.reverse` domain will be a registrar that permits the caller to take ownership of 
the reverse record for their own address. It provides the following method:

    function claim(address owner) returns (bytes32 node);

When called by account `x` it will instruct the ENS registry to transfer ownership of the name `hex(x) + '.addr.reverse'` to the provided address, and return the namehash of the ENS record thus transferred.

Allowing the caller to specify an owner other than themselves for the relevant node facilitates contracts that need accurate reverse ENS entries delegating this to their creators with a minimum of code inside their constructor:

    reverseRegistrar.claim(msg.sender)

## Resolver interface
A new resolver interface is defined, consisting of the following method:

    function name(bytes32 node) constant returns (string);

Resolvers that implement this interface must return a valid ENS name for the requested node, or the empty string if no name is defined for the requested node.

The interface ID of this interface is 0x691f3431.

Future EIPs may specify more record types appropriate to reverse ENS records.

# Appendix 1: Registrar implementation

This registrar, written in Solidity, implements the specifications outlined above.

    pragma solidity ^0.4.0;

    import 'interface.sol';

    contract ReverseRegistrar {
        AbstractENS public ens;
        bytes32 public rootNode;
        
        /**
         * @dev Constructor
         * @param ensAddr The address of the ENS registry.
         * @param node The node hash that this registrar governs.
         */
        function ReverseRegistrar(address ensAddr, bytes32 node) {
            ens = AbstractENS(ensAddr);
            rootNode = node;
        }
    
        /**
         * @dev Transfers ownership of the reverse ENS record associated with the
         *      calling account.
         * @param owner The address to set as the owner of the reverse record in ENS.
         * @return The ENS node hash of the reverse record.
         */
        function claim(address owner) returns (bytes32 node) {
            var label = sha3HexAddress(msg.sender);
            ens.setSubnodeOwner(rootNode, label, owner);
            return sha3(rootNode, label);
        }
    
        /**
         * @dev An optimised function to compute the sha3 of the lower-case
         *      hexadecimal representation of an Ethereum address.
         * @param addr The address to hash
         * @return The SHA3 hash of the lower-case hexadecimal encoding of the
         *         input address.
         */
        function sha3HexAddress(address addr) constant returns (bytes32 ret) {
            assembly {
                let lookup := 0x3031323334353637383961626364656600000000000000000000000000000000
                let i := 40
            loop:
                i := sub(i, 1)
                mstore8(i, byte(and(addr, 0xf), lookup))
                addr := div(addr, 0x10)
                i := sub(i, 1)
                mstore8(i, byte(and(addr, 0xf), lookup))
                addr := div(addr, 0x10)
                jumpi(loop, i)
                ret := sha3(0, 40)
            }
        }
    }


#eip-190.md
```
EIP: Draft
Title: Ethereum Smart Contract Packaging Standard
Authors: Piper Merriam, Tim Coulter, Denis Erfurt (mhhf), RJ Catalano (VoR0220), Iuri Matias (iurimatias)
Status: Draft
Type: Standards Track - ERC
Created: 2017-01-10
```

# Abstract

This ERC proposes a specification for Ethereum smart contract packages.  

The specification was collaboratively developed by the following Ethereum development framework maintainers.

* Tim Coulter (Truffle)
* Denis Erfurt (Dapple)
* Piper Merriam (Populus)
* RJ Catalano (Eris PM)
* Iuri Matias (Embark)

# Motivation

Packaging is a core piece of modern software development which is missing from the Ethereum ecosystem.  The lack of packaging limits the ability for developers to reuse code which negatively affects productivity and security.

A key example of this is the ERC20 standard.  There are a few well audited reusable token contracts available but most developers end up writing their own because of the difficulty in finding and reusing existing code.

A packaging standard should have the following positive effects on the ecosystem:

* Greater overall productivity caused by the ability to reuse existing code.
* Increased security caused by the ability to reuse existing well audited implementations of common patterns (ERC20, crowdfunding, etc).

Smart contract packaging should also have a direct positive effect on the end user.  Wallet software will be able to consume a released package and generate an interface for interacting with any deployed contracts included within that package.  With the advent of [ENS](https://github.com/ethereum/EIPs/issues/137) all of the pieces will be in place for a wallet to take a human readable name and present the user with an interface for interacting with the underlying application.


# Specification

The full specification for this standard is maintained separately in the repository [epm/epm-spec](https://github.com/ethpm/epm-spec).

This EIP refers to the `1.0.0` version of the specification: [https://github.com/ethpm/epm-spec/tree/v1.0.0](https://github.com/ethpm/epm-spec/tree/v1.0.0) 

The specification contains details for a single document referred to as a *"Release Lockfile"*.  

* Release Lockfile Specification: [https://github.com/ethpm/epm-spec/blob/v1.0.0/release-lockfile.spec.md](https://github.com/ethpm/epm-spec/blob/v1.0.0/release-lockfile.spec.md).
* JSON Schema for Release Lockfile: [https://github.com/ethpm/epm-spec/blob/v1.0.0/spec/release-lockfile.spec.json](https://github.com/ethpm/epm-spec/blob/v1.0.0/spec/release-lockfile.spec.json)

> These documents have not been inlined into this ERC to ensure that there is a single source of truth for the specification.


# Use Cases

This specification covers the following types of smart contract packages.

1. Packages with contracts intended to be used as base contract such as the common `owned` pattern.
2. Packages with contracts that are ready to use as-is such as an ERC20 token contract.
3. Packages with deployed contracts such as libraries or services.

Full explanations and examples of these use cases can be found in the [`README.md`](https://github.com/ethpm/epm-spec/blob/v1.0.0/README.md#use-cases) from the `epm/epm-spec` repository.


# Package Managers

The *Release Lockfile* is intended for consumption by package management software.  Specific care was made to ensure that all of the following functionality can be implemented by package managers.


## Deterministic builds

Ensures that a package will always resolve to the same set of dependencies and source files.  Both source files and dependencies are content addressed to ensure that the referenced resources cannot change.


## Bytecode verification

Contains the appropriate information for a package manager to inspect a deployed contract and verify that its bytecode matches the bytecode that results from compilation and linking of the package source code.


## Multi-chain deploys

Supports deployments across multiple chains, allowing a package to define addresses on both the public mainnet and testnet.


## Trusted packages

Allows for packages which exclude source code or other elements which would be needed for verification of the contract bytecode.  This allows for minimalistic packages to be created for special situations where the package manager will not be performing verification.


# Framework support and integration

Support for ERC190 is either implemented or in progress for the following:

* [Truffle](http://truffleframework.com/)
* [Populus](http://populus.readthedocs.io/en/latest/)
* [Dapple](http://dapple.readthedocs.io/en/master/)
* [Eris PM](https://github.com/eris-ltd/eris-cli)
* [Embark](https://github.com/iurimatias/embark-framework)
* [Browser Solidity](https://github.com/ethereum/browser-solidity/issues/386)


#eip-2.md
```
EIP: 2
Title: Homestead Hard-fork Changes
Author: Vitalik Buterin <v@buterin.com>
Status: Final
Type: Standard Track
Category: Core
Created: 2015-11-15
```

# Specification

If `block.number >= HOMESTEAD_FORK_BLKNUM` (e.g., 1.150.000 on livenet, 494.000 on Morden and 0 on future testnets), do the following:

1. The gas cost *for creating contracts via a transaction* is increased from 21000 to 53000, ie. if you send a transaction and the to address is the empty string, the initial gas subtracted is 53000 plus the gas cost of the tx data, rather than 21000 as is currently the case. Contract creation from a contract using the `CREATE` opcode is unaffected.
2. All transaction signatures whose s-value is greater than `secp256k1n/2` are now considered invalid. The ECDSA recover precompiled contract remains unchanged and will keep accepting high s-values - this is useful if e.g. a contract recovers old Bitcoin signatures.
3. If contract creation does not have enough gas to pay for the final gas fee for adding the contract code to the state, the contract creation fails (ie. goes out-of-gas) rather than leaving an empty contract.
4. Change the difficulty adjustment algorithm from the current formula: `block_diff = parent_diff + parent_diff // 2048 * (1 if block_timestamp - parent_timestamp < 13 else -1) + int(2**((block.number // 100000) - 2))` (where the ` + int(2**((block.number // 100000) - 2))` represents the exponential difficulty adjustment component) to `block_diff = parent_diff + parent_diff // 2048 * max(1 - (block_timestamp - parent_timestamp) // 10, -99) + int(2**((block.number // 100000) - 2))`, where `//` is the integer division operator, eg. `6 // 2 = 3`, `7 // 2 = 3`, `8 // 2 = 4`. The `minDifficulty` still defines the minimum difficulty allowed and no adjustment may take it below this.

# Rationale

Currently, there is an excess incentive to create contracts via transactions, where the cost is 21000, rather than contracts, where the cost is 32000. Additionally, with the help of suicide refunds, it is currently possible to make a simple ether value transfer using only 11664 gas; the code for doing this is as follows:

```python
from ethereum import tester as t
> from ethereum import utils
> s = t.state()
> c = s.abi_contract('def init():\n suicide(0x47e25df8822538a8596b28c637896b4d143c351e)', endowment=10**15)
> s.block.get_receipts()[-1].gas_used
11664
> s.block.get_balance(utils.normalize_address(0x47e25df8822538a8596b28c637896b4d143c351e))
1000000000000000
```
This is not a particularly serious problem, but is nevertheless arguably a bug.

Allowing transactions with any s value with `0 < s < secp256k1n`, as is currently the case, opens a transaction malleability concern, as one can take any transaction, flip the s value from `s` to `secp256k1n - s`, flip the v value (`27 -> 28`, `28 -> 27`), and the resulting signature would still be valid. This is not a serious security flaw, especially since Ethereum uses addresses and not transaction hashes as the input to an ether value transfer or other transaction, but it nevertheless creates a UI inconvenience as an attacker can cause the transaction that gets confirmed in a block to have a different hash from the transaction that any user sends, interfering with user interfaces that use transaction hashes as tracking IDs. Preventing high s values removes this problem.

Making contract creation go out-of-gas if there is not enough gas to pay for the final gas fee has the benefits that (i) it creates a more intuitive "success or fail" distinction in the result of a contract creation process, rather than the current "success, fail, or empty contract" trichotomy, (ii) makes failures more easily detectable, as unless contract creation fully succeeds then no contract account will be created at all, and (iii) makes contract creation safer in the case where there is an endowment, as there is a guarantee that either the entire initiation process happens or the transaction fails and the endowment is refunded.

The difficulty adjustment change conclusively solves a problem that the Ethereum protocol saw two months ago where an excessive number of miners were mining blocks that contain a timestamp equal to `parent_timestamp + 1`; this skewed the block time distribution, and so the current block time algorithm, which targets a *median* of 13 seconds, continued to target the same median but the mean started increasing. If 51% of miners had started mining blocks in this way, the mean would have increased to infinity. The proposed new formula is roughly based on targeting the mean; one can prove that with the formula in use an average block time longer than 24 seconds is mathematically impossible in the long term.

The use of `(block_timestamp - parent_timestamp) // 10` as the main input variable rather than the time difference directly serves to maintain the coarse-grained nature of the algorithm, preventing an excessive incentive to set the timestamp difference to exactly 1 in order to create a block that has slightly higher difficulty and that will thus be guaranteed to beat out any possible forks. The cap of -99 simply serves to ensure that the difficulty does not fall extremely far if two blocks happen to be very far apart in time due to a client security bug or other black-swan issue.

# Implementation

This is implemented in Python here:

1. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L130
2. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L129
3. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L304
4. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/blocks.py#L42


#eip-5.md
### Title

      EIP: 5
      Title: Gas Usage for `RETURN` and `CALL*`
      Author: Christian Reitwiessner <c@ethdev.com>
      Status: Draft
      Type: Standards Track
      Layer: Consensus (hard-fork)
      Created: 2015-11-22

### Abstract

This EIP makes it possible to call functions that return strings and other dynamically-sized arrays.
Currently, when another contract / function is called from inside the Ethereum Virtual Machine,
the size of the output has to be specified in advance. It is of course possible to give a larger
size, but gas also has to be paid for memory that is not written to, which makes returning
dynamically-sized data both costly and inflexible to the extent that it is actually unusable.

The solution proposed in this EIP is to charge gas only for memory that is actually written to at
the time the `CALL` returns.

### Specification

The gas and memory semantics for `CALL`, `CALLCODE` and `DELEGATECALL` (called later as `CALL*`)
are changed in the following way (`CREATE` does not write to memory and is thus unaffected):

Suppose the arguments to `CALL*` are `gas, address, value, input_start, input_size, output_start, output_size`,
then, at the beginning of the opcode, gas for growing memory is only charged for `input_start + input_size`, but not
for `output_start + output_size`.

If the called contract returns data of size `n`, the memory of the calling contract is grown to
`output_start + min(output_size, n)` (and the calling contract is charged gas for that) and the
output is written to the area `[output_start, output_start + min(n, output_size))`.

The calling contract can run out of gas both at the beginning of the opcode and at the end
of the opcode.

After the call, the `MSIZE` opcode should return the size the memory was actually grown to.

### Motivation

In general, it is good practise to reserve a certain memory area for the output of a call,
because letting a subroutine write to arbitrary areas in memory might be dangerous. On the
other hand, it is often hard to know the output size of a call prior to performing the call:
The data could be in the storage of another contract which is generally inaccessible and
determining its size would require another call to that contract.

Furthermore, charging gas for areas of memory that are not actually written to is unnecessary.

This proposal tries to solve both problems: A caller can choose to provide a gigantic area of
memory at the end of their memory area. The callee can "write" to it by returning and the
caller is only charged for the memory area that is actually written.

This makes it possible to return dynamic data like strings and dynamically-sized arrays
in a very flexible way. It is even possible to determine the size of the returned data:
If the caller uses `output_start = MSIZE` and `output_size = 2**256-1`, the area of
memory that was actually written to is `(output_start, MSIZE)` (here, `MSIZE` as evaluated
after the call). This is important because it allows "proxy" contracts
which call other contracts whose interface they do not know and just return their output,
i.e. they both forward the input and the output. For this, it is important that the caller
(1) does not need to know the size of the output in advance and (2) can determine the
size of the output after the call.


### Rationale

This way of dealing with the problem requires a minimal change to the Ethereum Virtual Machine.
Other means of achieving a similar goal would have changed the opcodes themselves or
the number of their arguments. Another possibility would have been to only change the
gas mechanics if `output_size` is equal to `2**256-1`. Since the main difficulty in the
implementation is that memory has to be enlarged at two points in the code around `CALL`,
this would not have been a simplification.

At an earlier stage, it was proposed to also add the size of the returned data on the stack,
but the `MSIZE` mechanism described above should be sufficient and is much better
backwards compatible.

Some comments are available at https://github.com/ethereum/EIPs/issues/8

### Backwards Compatibility

This proposal changes the semantics of contracts because contracts can access the gas counter
and the size of memory.

On the other hand, it is unlikely that existing contracts will suffer from this change due to
the following reasons:

Gas:

The VM will not charge more gas than before. Usually, contracts are written in a way such
that their semantics do not change if they use up less gas. If more gas were used, contracts
might go out-of-gas if they perform a tight estimation for gas needed by sub-calls. Here,
contracts might only return more gas to their callers.

Memory size:

The `MSIZE` opcode is typically used to allocate memory at a previously unused spot.
The change in semantics affects existing contracts in two ways:

1. Overlaps in allocated memory. By using `CALL`, a contract might have wanted to allocate
   a certain slice of memory, even if that is not written to by the called contract.
   Subsequent uses of `MSIZE` to allocate memory might overlap with this slice that is
   now smaller than before the change. It is though unlikely that such contracts exist.

2. Memory addresses change. Rather general, if memory is allocated using `MSIZE`, the
   addresses of objects in memory will be different after the change. Contract should
   all be written in a way, though, such that objects in memory are _relocatable_,
   i.e. their absolute position in memory and their relative position to other
   objects does not matter. This is of course not the case for arrays, but they
   are allocated in a single allocation and not with an intermidiate `CALL`.


### Implementation

VM implementers should take care not to grow the memory until the end of the call and after a check that sufficient
gas is still available. Typical uses of the EIP include "reserving" `2**256-1` bytes of memory for the output.

Python implementation:

  old: http://vitalik.ca/files/old.py
  new: http://vitalik.ca/files/new.py


#eip-55.md
```
EIP: 55
Title: Mixed-case checksum address encoding
Author: Vitalik Buterin
Type: Standard Track
Category: ERC
Status: Accepted
Created: 2016-01-14
```

# Specification

Code:

``` python
from ethereum import utils

def checksum_encode(addr): # Takes a 20-byte binary address as input
    o = ''
    v = utils.big_endian_to_int(utils.sha3(addr.hex()))
    for i, c in enumerate(addr.hex()):
        if c in '0123456789':
            o += c
        else:
            o += c.upper() if (v & (2**(255 - 4*i))) else c.lower()
    return '0x'+o

def test(addrstr):
    assert(addrstr == checksum_encode2(bytes.fromhex(addrstr[2:])))

test('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed')
test('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
test('0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB')
test('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb')

```

In English, convert the address to hex, but if the `i`th digit is a letter (ie. it's one of `abcdef`) print it in uppercase if the `4*i`th bit of the hash of the lowercase hexadecimal address is 1 otherwise print it in lowercase.

# Implementation

In javascript:

```js
const createKeccakHash = require('keccak')

function toChecksumAddress (address) {
  address = address.toLowerCase().replace('0x','');
  var hash = createKeccakHash('keccak256').update(address).digest('hex')
  var ret = '0x'

  for (var i = 0; i < address.length; i++) {
    if (parseInt(hash[i], 16) >= 8) {
      ret += address[i].toUpperCase()
    } else {
      ret += address[i]
    }
  }

  return ret
}
```

```
> toChecksumAddress('0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359')
'0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359'
```

Note that the input to the Keccak256 hash is the lowercase hexadecimal string (i.e. the hex address encoded as ASCII):

```
    var hash = createKeccakHash('keccak256').update(Buffer.from(address.toLowerCase(), 'ascii')).digest()
```

# Rationale

Benefits:
- Backwards compatible with many hex parsers that accept mixed case, allowing it to be easily introduced over time
- Keeps the length at 40 characters
- On average there will be 15 check bits per address, and the net probability that a randomly generated address if mistyped will accidentally pass a check is 0.0247%. This is a ~50x improvement over ICAP, but not as good as a 4-byte check code.

# Adoption

| Wallet                   | displays checksummed addresses | rejects invalid mixed-case | rejects too short | rejects too long |
|--------------------------|--------------------------------|----------------------------|-------------------|------------------|
| Jaxx 1.2.17              | No                             | Yes                        | Yes               | Yes              |
| MetaMask 3.7.8           | Yes                            | Yes                        | Yes               | Yes              |
| Mist 0.8.10              | Yes                            | Yes                        | Yes               | Yes              |
| MyEtherWallet v3.9.4     | Yes                            | Yes                        | Yes               | Yes              |
| Parity 1.6.6-beta (UI)   | Yes                            | Yes                        | Yes               | Yes              |

### Exchange support for mixed-case address checksums, as of 2017-05-27:

| Exchange     | displays checksummed deposit addresses | rejects invalid mixed-case | rejects too short | rejects too long |
|--------------|----------------------------------------|----------------------------|-------------------|------------------|
| Bitfinex     | No                                     | Yes                        | Yes               | Yes              |
| Coinbase     | Yes                                    | No                         | Yes               | Yes              |
| GDAX         | Yes                                    | Yes                        | Yes               | Yes              |
| Kraken       | No                                     | No                         | Yes               | Yes              |
| Poloniex     | No                                     | No                         | Yes               | Yes              |
| Shapeshift   | No                                     | No                         | Yes               | Yes              |

# References

1. EIP 55 issue and discussion https://github.com/ethereum/eips/issues/55
2. Python example by @Recmo https://github.com/ethereum/eips/issues/55#issuecomment-261521584
3. Python implementation in [`ethereum-utils`](https://github.com/pipermerriam/ethereum-utils#to_checksum_addressvalue---text)
4. Ethereumjs-util implementation https://github.com/ethereumjs/ethereumjs-util/blob/75f529458bc7dc84f85fd0446d0fac92d991c262/index.js#L452-L466


#eip-6.md
### Title

      EIP: 6
      Title: Renaming SUICIDE opcode
      Author: Hudson Jameson <hudson@hudsonjameson.com>
      Status: Final
      Type: Standards Track
      Layer: Applications
      Created: 2015-11-22

### Abstract
The solution proposed in this EIP is to change the name of the `SUICIDE` opcode in Ethereum programming languages with `SELFDESTRUCT`.

### Motivation
Mental health is a very real issue for many people and small notions can make a difference. Those dealing with loss or depression would benefit from not seeing the word suicide in our a programming languages. By some estimates, 350 million people worldwide suffer from depression. The semantics of Ethereum's programming languages need to be reviewed often if we wish to grow our ecosystem to all types of developers.

An Ethereum security audit commissioned by DEVolution, GmbH and [performed by Least Authority](https://github.com/LeastAuthority/ethereum-analyses/blob/master/README.md) recommended the following:
> Replace the instruction name "suicide" with a less connotative word like "self-destruct", "destroy", "terminate", or "close", especially since that is a term describing the natural conclusion of a contract.

The primary reason for us to change the term suicide is to show that people matter more than code and Ethereum is a mature enough of a project to recognize the need for a change. Suicide is a heavy subject and we should make every effort possible to not affect those in our development community who suffer from depression or who have recently lost someone to suicide. Ethereum is a young platform and it will cause less headaches if we implement this change early on in it's life.

### Implementation
`SELFDESTRUCT` is added as an alias of `SUICIDE` opcode (rather than replacing it).
https://github.com/ethereum/solidity/commit/a8736b7b271dac117f15164cf4d2dfabcdd2c6fd
https://github.com/ethereum/serpent/commit/1106c3bdc8f1bd9ded58a452681788ff2e03ee7c


#eip-615.md
```
EIP: 615
Title: Subroutines and Static Jumps for the EVM
Status: Draft
Type: Core
Author: Greg Colvin <greg@colvin.org>, Paweł Bylica, Christian Reitwiessner
Created: 2016-12-10
Edited: 2017-25-4
```
## Abstract

This EIP introduces new EVM opcodes and conditions on EVM code to support subroutines and static jumps, disallow dynamic jumps, and thereby make EVM code amenable to linear-time static analysis.  This will provide for better compilation, interpretation, transpilation, and formal analysis of EVM code.

## MOTIVATION

All current implementations of the Ethereum Virtual Machine, including the just-in-time compilers, are much too slow. This proposal identifies a major reason for this and proposes changes to the EVM specification to address the problem.

In particular, it imposes restrictions on current EVM code and proposes new instructions to help provide for
* better-optimized compilation to native code
* faster interpretation
* faster transpilation to eWASM
* better compilation from other languages,
   including eWASM and Solidity
* better formal analysis tools

These goals are achieved by
* disallowing dynamic jumps
* introducing subroutines - jumps with return support
* disallowing pathological control flow and uses of the stack

We also propose to validate - in linear time - that EVM contracts correctly use subroutines, avoid misuse of the stack, and meet other safety conditions _before_ placing them on the blockchain.  Validated code precludes most runtime exceptions and the need to test for them.  And well-behaved control flow and use of the stack makes life easier for interpreters, compilers, formal analysis, and other tools.

## THE PROBLEM

Currently the EVM supports dynamic jumps, where the address to jump to is an argument on the stack. These dynamic jumps obscure the structure of the code and thus mostly inhibit control- and data-flow analysis.  This puts the quality and speed of optimized compilation fundamentally at odds.  Further, since every jump can potentially be to any jump destination in the code, the number of possible paths through the code goes up as the product of the number of jumps by the number of destinations, as does the time complexity of static analysis.  But absent dynamic jumps code can be statically analyzed in linear time.

Static analysis includes validation, and much of optimization, compilation, transpilation, and formal analysis; every part of the tool chain benefits when linear-time analysis is available.  In particular, faster control-flow analysis means faster compilation of EVM code to native code, and better data-flow analysis can help the compiler and the interpreter better track the size of the values on the stack and use native 64- and 32-bit operations when possible.  Also, conditions which are checked at validation time don’t have to be checked repeatedly at runtime.

Note that analyses of a contract’s bytecode before execution - such as optimizations performed before interpretation, JIT compilation, and on-the-fly machine code generation - must be efficient and linear-time. Otherwise, specially crafted contracts can be used as attack vectors against clients that use static analysis of EVM code before the creation or execution of contracts.

## PROPOSAL

We propose to deprecate two existing instructions - `JUMP` and `JUMPI`. They take their argument on the stack, which means that unless the value is constant they can jump to any `JUMPDEST`.  (In simple cases like `PUSH 0 JUMP` the value on the stack can be known to be constant, but in general it's difficult.)  We must nonetheless continue to support them in old code.

Having deprecated `JUMP` and `JUMPI`, we propose new instructions to support their legitimate uses.

### Preliminaries

These forms
* `INSTRUCTION x,`
* `INSTRUCTION x, y`
* `INSTRUCTION n, x ...`

name instructions with one, two, and two or more arguments, respectively.  An instruction is represented in the bytecode as a single-byte opcode.  The arguments are laid out as immediate data bytes following the opcode.  The size and encoding of immediate data fields is open to change.  In particular, easily-parsed variable-length encodings might prove useful for bytecode offsets - which are in practice small but in principle can be large.

### Primitives

The two most important uses of `JUMP` and `JUMPI` are static jumps and return jumps. Conditional and unconditional static jumps are the mainstay of control flow.  Return jumps are implemented as a dynamic jump to a return address pushed on the stack.  With the combination of a static jump and a dynamic return jump you can - and Solidity does - implement subroutines.  The problem is that static analysis cannot tell the one place the return jump is going, so it must analyze every possibility.

Static jumps are provided by
* `JUMPTO jump_target`
* `JUMPIF jump_target`
which are the same as `JUMP` and `JUMPI` except that they jump to an immediate `jump_target`, given as four immediate bytes, rather than an address on the stack.

To support subroutines, `BEGINSUB`, `JUMPSUB`, and `RETURNSUB` are provided.  Brief descriptions follow, and full semantics are given below.

* `BEGINSUB n_args, n_results`
marks the **single** entry to a subroutine.  `n_args` items are taken off of the stack at entry to, and `n_results` items are placed on the stack at return from the subroutine. `n_args` and `n_results` are given as one immediate byte each.  The bytecode for a subroutine ends at the next `BEGINSUB` instruction (or `BEGINDATA`, below) or at the end of the bytecode.

* `JUMPSUB jump_target`
jumps to an immediate subroutine address, given as four immediate bytes.

* `RETURNSUB`
returns from the current subroutine to the instruction following the JUMPSUB that entered it.

These five simple instructions form the primitives of the proposal.

### Data

In order to validate subroutines, EVM bytecode must be sequentially scanned matching jumps to their destinations.  Since creation code has to contain the runtime code as data, that code might not correctly validate in the creation context and also does not have to be validated prior to the execution of the creation code. Because of that, there needs to be a way to place data into the bytecode that will be skipped over and not validated.  Such data will prove useful for other purposes as well.

* `BEGINDATA`
specifies that all of the following bytes to the end of the bytecode are data, and not reachable code.

### Indirect Jumps

The primitive operations provide for static jumps.  Dynamic jumps are also used for O(1) indirection: an address to jump to is selected to push on the stack and be jumped to.  So we also propose two more instructions to provide for constrained indirection.  We support these with vectors of `JUMPDEST` or `BEGINSUB` offsets stored inline, which can be selected with an index on the stack.  That constrains validation to a specified subset of all possible destinations.  The danger of quadratic blow up is avoided because it takes as much space to store the jump vectors as it does to code the worst case exploit. 

Dynamic jumps to a `JUMPDEST` are used to implement O(1) jumptables, which are useful for dense switch statements, and are implemented as instructions similar to this one on most CPUs.
* `JUMPV n, jumpdest ...`
jumps to one of a vector of `n` `JUMPDEST` offsets via a zero-based index on the stack.  The vector is stored inline in the bytecode.  If the index is greater than or equal to `n - 1` the last (default) offset is used.  `n` is given as four immediate bytes, all `JUMPDEST` offsets as four immediate bytes each.

Dynamic jumps to a `BEGINSUB` are used to implement O(1) virtual functions and callbacks, which take just two pointer dereferences on most CPUs.
* `JUMPSUBV n, beginsub ...`
jumps to one of a vector of `n` `BEGINSUB` offsets via a zero-based index on the stack.  The vector is stored inline in the bytecode, MSB-first.  If the index is greater than or equal to `n - 1` the last (default) offset is used.  `n` is given as four immediate bytes, the `n` offsets as four immediate bytes each.

`JUMPV` and `JUMPSUBV` are not strictly necessary.  They provide O(1) operations that can be replaced by O(n) or O(log n) EVM code using static jumps, but that code will be slower, larger and use more gas for things that can and should be fast, small, and cheap, and that are directly supported in WASM with br_table and call_indirect.

### Variable Access

These operations provide convenient access to subroutine parameters and other variables at fixed stack offsets within a subroutine.

* `PUTLOCAL n`
Pops the top value on the stack and copies it to local variable `n`.

* `GETLOCAL n`
Pushes the value of local variable `n` on the EVM stack.

Local variable `n` is `FP[-n]` as defined below.

## SEMANTICS

Jumps to and returns from subroutines are described here in terms of
* the EVM data stack, (as defined in the [Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf) usually just called “the stack”,
* a return stack of `JUMPSUB` and `JUMPSUBV` offsets, and
* a frame stack of frame pointers.

We will adopt the following conventions to describe the machine state:
* The _program counter_ `PC` is (as usual) the byte offset of the currently executing instruction.
* The _stack pointer_ `SP` corresponds to the number of items on the stack - the _stack size_.  As a negative offset it addresses the current top of the stack of data values, where new items are pushed.
* The _frame pointer_ `FP` is set to `SP + n_args` at entry to the currently executing subroutine.
* The _stack items_ between the frame pointer and the current stack pointer are called the _frame_.
* The current number of items in the frame, `FP - SP`, is the _frame size_.

Defining the frame pointer so as to include the arguments is unconventional, but better fits our stack semantics and simplifies the remainder of the proposal.

The frame pointer and return stacks are internal to the subroutine mechanism, and not directly accessible to the program.  This is necessary to prevent the program from modifying its state in ways that could be invalid.

The first instruction of an array of EVM bytecode begins execution of a _main_ routine with no arguments, `SP` and `FP` set to 0, and with one value on the return stack - `code size - 1`. (Executing the virtual byte of 0 after this offset causes an EVM to stop.  Thus executing a `RETURNSUB` with no prior `JUMPSUB` or `JUMBSUBV` - that is, in the _main_ routine - executes a `STOP`.)

Execution of a subroutine begins with `JUMPSUB` or `JUMPSUBV`, which
* push `PC` on the return stack,
* push `FP` on the frame stack,
thus suspending execution of the current subroutine, and
* set `FP` to `SP + n_args`, and
* set `PC` to the specified `BEGINSUB` address,
thus beginning execution of the new subroutine.
(The _main_ routine is not addressable by `JUMPSUB` instructions.)

Execution of a subroutine is suspended during and resumed after execution of nested subroutines, and ends upon encountering a `RETURNSUB`, which
* sets `FP` to the top of the virtual frame stack and pops the stack, and
* sets `PC` to top of the return stack and pops the stack
* advances `PC` to the next instruction
thus resuming execution of the enclosing subroutine or _main_ program.
A `STOP or `RETURN` also ends the execution of a subroutine.

## VALIDITY

We would like to consider EVM code valid if and only if no execution of the program can lead to an exceptional halting state.  But we must and will validate code in linear time.  So our validation does not consider the code’s data and computations, only its control flow and stack use.  This means we will reject programs with invalid code paths, even if those paths cannot be executed at runtime.  Most conditions can be validated, and will not need to be checked at runtime; the exceptions are sufficient gas and sufficient stack.  So some false negatives and runtime checks are the price we pay for linear time validation.

_Execution_ is as defined in the Yellow Paper - a sequence of changes in the EVM state.  The conditions on valid code are preserved by state changes.  At runtime, if execution of an instruction would violate a condition the execution is in an exceptional halting state.  The yellow paper defines five such states.
>1  Insufficient gas

>2  More than 1024 stack items

>3  Insufficient stack items

>4  Invalid jump destination

>5  Invalid instruction

We propose to expand and extend the Yellow Paper conditions to handle the new instructions we propose. 

To handle the return stack we expand the conditions on stack size:
>2a  The size of the data stack does not exceed 1024.

>2b  The size of the return stack does not exceed 1024.

Given our more detailed description of the data stack we restate condition 3 - stack underflow - as
>3  `SP` must be less than or equal to `FP`

Since the various `DUP` and `SWAP` operations are formalized as taking items off the stack and putting them back on, this prevents `DUP` and `SWAP` from accessing data below the frame pointer, since taking too many items off of the stack would mean that `SP` is less than `FP`.

To handle the new jump instructions and subroutine boundaries we expand the conditions on jumps and jump destinations.
>4a  `JUMPTO`, `JUMPIF`, and `JUMPV` address only `JUMPDEST` instructions.

>4b  `JUMPSUB` and `JUMPSUBV` address only `BEGINSUB` instructions.

>4c  `JUMP` instructions do not address instructions outside of the subroutine they occur in.

We have two new conditions on execution to ensure consistent use of the stack by subroutines:
>6  For `JUMPSUB` and `JUMPSUBV` the frame size is at least the `n_args` of the `BEGINSUB`(s) to jump to.

>7  For `RETURNSUB` the frame size is equal to the `n_results` of the enclosing `BEGINSUB`.

Finally, we have one condition that prevents pathological uses of the stack:
>8  For every instruction in the code the frame size is constant.

In practice, we must test at runtime for conditions 1 and 2 - sufficient gas and sufficient stack.  We don’t know how much gas there will be, we don’t know how deep a recursion may go, and analysis of stack depth even for non-recursive programs is non-trivial.

All of the remaining conditions we validate statically.

## VALIDATION

Validation comprises two tasks:
* Checking that jump destinations are correct and instructions valid.
* Checking that subroutines satisfy the conditions on control flow and stack use.

We sketch out these two validation functions in pseudo-C below.   To simplify the presentation only the five primitives are handled (`JUMPV` and `JUMPSUBV` would just add more complexity to loop over their vectors), we assume helper functions for extracting instruction arguments from immediate data and managing the stack pointer and program counter, and some optimizations are forgone.

### Validating jumps

Validating that jumps are to valid addresses takes two sequential passes over the bytecode - one to build sets of jump destinations and subroutine entry points, another to check that addresses jumped to are in the appropriate sets.
```
    bytecode[code_size]   // contains EVM bytecode to validate
    is_sub[code_size]     // is there a BEGINSUB at PC?
    is_dest[code_size]    // is there a JUMPDEST at PC?
    sub_for_pc[code_size] // which BEGINSUB is PC in?
    
    bool validate_jumps(PC)
    {
        current_sub = PC

        // build sets of BEGINSUBs and JUMPDESTs
        for (PC = 0; instruction = bytecode[PC]; PC = advance_pc(PC))
        {
            if instruction is invalid
                return false
            if instruction is BEGINDATA
                return true
            if instruction is BEGINSUB
                is_sub[PC] = true
                current_sub = PC
                sub_for_pc[PC] = current_sub
            if instruction is JUMPDEST
                is_dest[PC] = true
            sub_for_pc[PC] = current_sub
        }
        
        // check that targets are in subroutine
        for (PC = 0; instruction = bytecode[PC]; PC = advance_pc(PC))
        {
            if instruction is BEGINDATA
                break;
            if instruction is BEGINSUB
                current_sub = PC
            if instruction is JUMPSUB
                if is_sub[jump_target(PC)] is false
                    return false
            if instruction is JUMPTO or JUMPIF
                if is_dest[jump_target(PC)] is false
                    return false
            if sub_for_pc[PC] is not current_sub
                return false
       }
        return true
    }
```
Note that code like this is already run by EVMs to check dynamic jumps, including building the jump destination set every time a contract is run, and doing a lookup in the jump destination set before every jump.

### Validating subroutines

This function can be seen as a symbolic execution of a subroutine in the EVM code, where only the effect of the instructions on the state being validated is computed.  Thus the structure of this function is very similar to an EVM interpreter.  This function can also be seen as an acyclic traversal of the directed graph formed by taking instructions as vertexes and sequential and branching connections as edges, checking conditions along the way.  The traversal is accomplished via recursion, and cycles are broken by returning when a vertex which has already been visited is reached.  The time complexity of this traversal is O(n-vertices + n-edges)

The basic approach is to call `validate_subroutine(i, 0, 0)`, for _i_ equal to the first instruction in the EVM code through each `BEGINDATA` offset.  `validate_subroutine()` traverses instructions sequentially, recursing when `JUMP` and `JUMPI` instructions are encountered.  When a destination is reached that has been visited before it returns, thus breaking cycles.  It returns true if the subroutine is valid, false otherwise.

```
    bytecode[code_size]     // contains EVM bytecode to validate
    frame_size[code_size ]  // is filled with -1

    // we validate each subroutine individually, as if at top level
    // * PC is the offset in the code to start validating at
    // * return_pc is the top PC on return stack that RETURNSUB returns to
    // * at top level FP = 0, so SP is both the frame size and the stack size
    validate_subroutine(PC, return_pc, SP)
    {
        // traverse code sequentially, recurse for jumps
        while true
        {
            instruction = bytecode[PC]

            // if frame size set we have been here before
            if frame_size[PC] >= 0
            {
                // check for constant frame size
                if instruction is JUMPDEST
                    if SP != frame_size[PC]
                        return false

                // return to break cycle
                return true
            }
            frame_size[PC] = SP

            // effect of instruction on stack
            n_removed = removed_items(instructions)
            n_added = added_items(instruction)

            // check for stack underflow
            if SP < n_removed
                return false

            // net effect of removing and adding stack items
            SP -= n_removed
            SP += n_added

            // check for stack overflow
            if SP > 1024
                return false

            if instruction is STOP, RETURN, SUICIDE or BEGINDATA
                return true	   

            // violates single entry
            if instruction is BEGINSUB
                 return false

            // return to top or from recursion to JUMPSUB
            if instruction is RETURNSUB
                break;

            if instruction is JUMPSUB
            {
                // check for enough arguments
                sub_pc = jump_target(PC)
                if SP < n_args(sub_pc)
                    return false
                return true
            }

            // reset PC to destination of jump
            if instruction is JUMPTO
            {
                PC = jump_target(PC)
                continue 
            }

            // recurse to jump to code to validate 
            if instruction is JUMPIF
            {
                if not validate_subroutine(jump_target(PC), return_pc, SP)
                    return false
            }

            // advance PC according to instruction
            PC = advance_pc(PC)
        }

        // check for right number of results
        if SP != n_results(return_pc)
            return false
        return true
    }
```

### COSTS & CODES

All of the instructions are O(1) with a small constant, requiring just a few machine operations each, whereas a `JUMP` or `JUMPI` must do an O(log n) binary search of an array of `JUMPDEST` offsets before every jump. With the cost of `JUMPI` being _high_ and the cost of `JUMP` being _mid_, we suggest the cost of `JUMPV` and `JUMPSUBV` should be _mid_, `JUMPSUB` and `JUMPIF` should be _low_, and`JUMPTO` should be _verylow_.  Measurement will tell.

We tentatively suggest the following opcodes:
```
0xB0 JUMPTO
0xB1 JUMPIF
0XB2 JUMPSUB
0xB4 JUMPSUBV
0xB5 BEGINSUB
0xB6 BEGINDATA
0xB8 RETURNSUB
0xB9 PUTLOCAL
0xBA GETLOCAL
```

### GETTING THERE FROM HERE

These changes would need to be implemented in phases at decent intervals:
>1 If this EIP is accepted, invalid code should be deprecated. Tools should stop generating invalid code, users should stop writing it, and clients should warn about loading it.

>2 A later hard fork would require clients to place only valid code on the block chain.  Note that despite the fork old EVM code will still need to be supported indefinitely.

If desired, the period of deprecation can be extended indefinitely by continuing to accept code not versioned as new - but without validation.  That is, by delaying step 2.  Since we must continue to run old code this is not technically difficult. 

Implementation of this proposal need not be difficult,  At the least, interpreters can simply be extended with the new opcodes and run unchanged otherwise.  The new opcodes require only stacks for the frame pointers and return offsets and the few pushes, pops, and assignments described above.  JIT code can use native calls.  Further optimizations include minimizing runtime checks for exceptions and taking advantage of validated code wherever possible.


#eip-7.md
### Title
      EIP: 7
      Title: DELEGATECALL
      Author: Vitalik Buterin <v@buterin.com>
      Status: Final
      Type: Homestead feature
      Created: 2015-11-15

### Overview

Add a new opcode, `DELEGATECALL` at `0xf4`, which is similar in idea to `CALLCODE`, except that it propagates the sender and value from the parent scope to the child scope, ie. the call created has the same sender and value as the original call.

### Specification

`DELEGATECALL`: `0xf4`, takes 6 operands:
- `gas`: the amount of gas the code may use in order to execute;
- `to`: the destination address whose code is to be executed;
- `in_offset`: the offset into memory of the input;
- `in_size`: the size of the input in bytes;
- `out_offset`: the offset into memory of the output;
- `out_size`: the size of the scratch pad for the output.

#### Notes on Gas
- The basic stipend is not given; `gas` is the total amount the callee receives.
- Like `CALLCODE`, account creation never happens, so the upfront gas cost is always `schedule.callGas` + `gas`.
- Unused gas is refunded as normal.

#### Notes on Sender
- `CALLER` and `VALUE` behave exactly in the callee's environment as they do in the caller's environment.

#### Other Notes
- The depth limit of 1024 is still preserved as normal.

### Rationale

Propagating the sender and value from the parent scope to the child scope makes it much easier for a contract to store another address as a mutable source of code and ''pass through'' calls to it, as the child code would execute in essentially the same environment (except for reduced gas and increased callstack depth) as the parent.

Use case 1: split code to get around 3m gas barrier

```python
~calldatacopy(0, 0, ~calldatasize())
if ~calldataload(0) < 2**253:
    ~delegate_call(msg.gas - 10000, $ADDR1, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
elif ~calldataload(0) < 2**253 * 2:
    ~delegate_call(msg.gas - 10000, $ADDR2, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
...
```

Use case 2: mutable address for storing the code of a contract:

```python
if ~calldataload(0) / 2**224 == 0x12345678 and self.owner == msg.sender:
    self.delegate = ~calldataload(4)
else:
    ~delegate_call(msg.gas - 10000, self.delegate, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
```
The child functions called by these methods can now freely reference `msg.sender` and `msg.value`.

### Possible arguments against

* You can replicate this functionality by just sticking the sender into the first twenty bytes of the call data. However, this would mean that code would need to be specially compiled for delegated contracts, and would not be usable in delegated and raw contexts at the same time.


#eip-8.md
### Title

      EIP: 8
      Title: devp2p Forward Compatibility Requirements for Homestead
      Author: Felix Lange <felix@ethdev.com>
      Status: Final
      Type: Standards Track
      Layer: Networking
      Created: 2015-12-18

### Abstract

This EIP introduces new forward-compatibility requirements for implementations of the
devp2p Wire Protocol, the RLPx Discovery Protocol and the RLPx TCP Transport Protocol.
Clients which implement EIP-8 behave according to Postel's Law:

> Be conservative in what you do, be liberal in what you accept from others.

### Specification

Implementations of **the devp2p Wire Protocol** should ignore the version number of hello
packets. When sending the hello packet, the version element should be set to the highest
devp2p version supported. Implementations should also ignore any additional list elements
at the end of the hello packet.

Similarly, implementations of **the RLPx Discovery Protocol** should not validate the
version number of the ping packet, ignore any additional list elements in any packet, and
ignore any data after the first RLP value in any packet. Discovery packets with unknown
packet type should be discarded silently. The maximum size of any discovery packet is
still 1280 bytes.

Finally, implementations of **the RLPx TCP Transport protocol** should accept a new
encoding for the encrypted key establishment handshake packets. If an EIP-8 style RLPx
`auth-packet` is received, the corresponding `ack-packet` should be sent using the rules
below.

Decoding the RLP data in `auth-body` and `ack-body` should ignore mismatches of `auth-vsn`
and `ack-vsn`, any additional list elements and any trailing data after the list. During
the transitioning period (i.e. until the old format has been retired), implementations
should pad `auth-body` with at least 100 bytes of junk data. Adding a random amount in
range [100, 300] is recommended to vary the size of the packet.

```text
auth-vsn         = 4
auth-size        = size of enc-auth-body, encoded as a big-endian 16-bit integer
auth-body        = rlp.list(sig, initiator-pubk, initiator-nonce, auth-vsn)
enc-auth-body    = ecies.encrypt(recipient-pubk, auth-body, auth-size)
auth-packet      = auth-size || enc-auth-body

ack-vsn          = 4
ack-size         = size of enc-ack-body, encoded as a big-endian 16-bit integer
ack-body         = rlp.list(recipient-ephemeral-pubk, recipient-nonce, ack-vsn)
enc-ack-body     = ecies.encrypt(initiator-pubk, ack-body, ack-size)
ack-packet       = ack-size || enc-ack-body

where

X || Y
    denotes concatenation of X and Y.
X[:N]
    denotes an N-byte prefix of X.
rlp.list(X, Y, Z, ...)
    denotes recursive encoding of [X, Y, Z, ...] as an RLP list.
sha3(MESSAGE)
    is the Keccak256 hash function as used by Ethereum.
ecies.encrypt(PUBKEY, MESSAGE, AUTHDATA)
    is the asymmetric authenticated encryption function as used by RLPx.
    AUTHDATA is authenticated data which is not part of the resulting ciphertext,
    but written to HMAC-256 before generating the message tag.
```

### Motivation

Changes to the devp2p protocols are hard to deploy because clients running an older
version will refuse communication if the version number or structure of the hello
(discovery ping, RLPx handshake) packet does not match local expectations.

Introducing forward-compatibility requirements as part of the Homestead consensus upgrade
will ensure that all client software in use on the Ethereum network can cope with future
network protocol upgrades (as long as backwards-compatibility is maintained).

### Rationale

The proposed changes address forward compatibility by applying Postel's Law (also known as
the Robustness Principle) throughout the protocol stack. The merit and applicability of
this approach has been studied repeatedly since its original application in RFC 761. For a
recent perspective, see
["The Robustness Principle Reconsidered" (Eric Allman, 2011)](http://queue.acm.org/detail.cfm?id=1999945).

#### Changes to the devp2p Wire Protocol

All clients currently contain statements such as the following:

```python
# pydevp2p/p2p_protocol.py
if data['version'] != proto.version:
    log.debug('incompatible network protocols', peer=proto.peer,
        expected=proto.version, received=data['version'])
    return proto.send_disconnect(reason=reasons.incompatibel_p2p_version)
```

These checks make it impossible to change the version or structure of the hello packet.
Dropping them enables switching to a newer protocol version: Clients implementing a newer
version simply send a packet with higher version and possibly additional list elements.

* If such a packet is received by a node with lower version, it will blindly assume that
  the remote end is backwards-compatible and respond with the old handshake.
* If the packet is received by a node with equal version, new features of the protocol can
  be used.
* If the packet is received by a node with higher version, it can enable
  backwards-compatibility logic or drop the connection.

#### Changes to the RLPx Discovery Protocol

The relaxation of discovery packet decoding rules largely codifies current practice. Most
existing implementations do not care about the number of list elements (an exception being
go-ethereum) and do not reject nodes with mismatching version. This behaviour is not
guaranteed by the spec, though.

If adopted, the change makes it possible to deploy protocol changes in a similar manner to
the devp2p hello change: simply bump the version and send additional information. Older
clients will ignore the additional elements and can continue to operate even when the
majority of the network has moved on to a newer protocol.

#### Changes to the RLPx TCP Handshake

Discussions of the RLPx v5 changes (chunked packets, change to key derivation) have
faltered in part because the v4 handshake encoding provides only one in-band way to add a
version number: shortening the random portion of the nonce. Even if the RLPx v5 handshake
proposal were accepted, future upgrades are hard because the handshake packet is a fixed
size ECIES ciphertext with known layout.

I propose the following changes to the handshake packets:

* Adding the length of the ciphertext as a plaintext header.
* Encoding the body of the handshake as RLP.
* Adding a version number to both packets in place of the token flag (unused).
* Removing the hash of the ephemeral public key (it is redundant).

These changes make it possible to upgrade the RLPx TCP transport protocol in the same
manner as described for the other protocols, i.e. by adding list elements and bumping the
version. Since this is the first change to the RLPx handshake packet, we can seize the
opportunity to remove all currently unused fields.

Additional data is permitted (and in fact required) after the RLP list because the
handshake packet needs to grow in order to be distinguishable from the old format.
Clients can employ logic such as the following pseudocode to handle both formats
simultaneously.

```go
packet = read(307, connection)
if decrypt(packet) {
    // process as old format
} else {
    size = unpack_16bit_big_endian(packet)
    packet += read(size - 307 + 2, connection)
    if !decrypt(packet) {
        // error
    }
    // process as new format
}
```

The plain text size prefix is perhaps the most controversial aspect of this document. It
has been argued that the prefix aids adversaries that seek to filter and identify RLPx
connections on the network level.

This is largely a question of how much effort the adversary is willing to expense. If the
recommendation to randomise the lengths is followed, pure pattern-based packet
recognition is unlikely to succeed.

* For typical firewall operators, blocking all connections whose first two bytes form an
  integer in range [300,600] is probably too invasive. Port-based blocking would be
  a more effective measure to filter most RLPx traffic.
* For an attacker who can afford to correlate many criteria, the size prefix would ease
  recognition because it adds to the indicator set. However, such an attacker could also
  be expected to read or participate in RLPx Discovery traffic, which would be sufficient
  to enable blocking of RLPx TCP connections whatever their format is.

### Backwards Compatibility

This EIP is backwards-compatible, all valid version 4 packets are still accepted.

### Implementation

[go-ethereum](https://github.com/ethereum/go-ethereum/pull/2091)
[libweb3core](https://github.com/ethereum/libweb3core/pull/46)
[pydevp2p](https://github.com/ethereum/pydevp2p/pull/32)

### Test Vectors

#### devp2p Base Protocol

devp2p hello packet advertising version 22 and containing a few additional list elements:

```text
f87137916b6e6574682f76302e39312f706c616e39cdc5836574683dc6846d6f726b1682270fb840
fda1cff674c90c9a197539fe3dfb53086ace64f83ed7c6eabec741f7f381cc803e52ab2cd55d5569
bce4347107a310dfd5f88a010cd2ffd1005ca406f1842877c883666f6f836261720304
```

#### RLPx Discovery Protocol

Implementations should accept the following encoded discovery packets as valid.
The packets are signed using the secp256k1 node key

```text
b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291
```

ping packet with version 4, additional list elements:

```text
e9614ccfd9fc3e74360018522d30e1419a143407ffcce748de3e22116b7e8dc92ff74788c0b6663a
aa3d67d641936511c8f8d6ad8698b820a7cf9e1be7155e9a241f556658c55428ec0563514365799a
4be2be5a685a80971ddcfa80cb422cdd0101ec04cb847f000001820cfa8215a8d790000000000000
000000000000000000018208ae820d058443b9a3550102
```

ping packet with version 555, additional list elements and additional random data:

```text
577be4349c4dd26768081f58de4c6f375a7a22f3f7adda654d1428637412c3d7fe917cadc56d4e5e
7ffae1dbe3efffb9849feb71b262de37977e7c7a44e677295680e9e38ab26bee2fcbae207fba3ff3
d74069a50b902a82c9903ed37cc993c50001f83e82022bd79020010db83c4d001500000000abcdef
12820cfa8215a8d79020010db885a308d313198a2e037073488208ae82823a8443b9a355c5010203
040531b9019afde696e582a78fa8d95ea13ce3297d4afb8ba6433e4154caa5ac6431af1b80ba7602
3fa4090c408f6b4bc3701562c031041d4702971d102c9ab7fa5eed4cd6bab8f7af956f7d565ee191
7084a95398b6a21eac920fe3dd1345ec0a7ef39367ee69ddf092cbfe5b93e5e568ebc491983c09c7
6d922dc3
```

pong packet with additional list elements and additional random data:

```text
09b2428d83348d27cdf7064ad9024f526cebc19e4958f0fdad87c15eb598dd61d08423e0bf66b206
9869e1724125f820d851c136684082774f870e614d95a2855d000f05d1648b2d5945470bc187c2d2
216fbe870f43ed0909009882e176a46b0102f846d79020010db885a308d313198a2e037073488208
ae82823aa0fbc914b16819237dcd8801d7e53f69e9719adecb3cc0e790c57e91ca4461c9548443b9
a355c6010203c2040506a0c969a58f6f9095004c0177a6b47f451530cab38966a25cca5cb58f0555
42124e
```

findnode packet with additional list elements and additional random data:

```text
c7c44041b9f7c7e41934417ebac9a8e1a4c6298f74553f2fcfdcae6ed6fe53163eb3d2b52e39fe91
831b8a927bf4fc222c3902202027e5e9eb812195f95d20061ef5cd31d502e47ecb61183f74a504fe
04c51e73df81f25c4d506b26db4517490103f84eb840ca634cae0d49acb401d8a4c6b6fe8c55b70d
115bf400769cc1400f3258cd31387574077f301b421bc84df7266c44e9e6d569fc56be0081290476
7bf5ccd1fc7f8443b9a35582999983999999280dc62cc8255c73471e0a61da0c89acdc0e035e260a
dd7fc0c04ad9ebf3919644c91cb247affc82b69bd2ca235c71eab8e49737c937a2c396
```

neighbours packet with additional list elements and additional random data:

```text
c679fc8fe0b8b12f06577f2e802d34f6fa257e6137a995f6f4cbfc9ee50ed3710faf6e66f932c4c8
d81d64343f429651328758b47d3dbc02c4042f0fff6946a50f4a49037a72bb550f3a7872363a83e1
b9ee6469856c24eb4ef80b7535bcf99c0004f9015bf90150f84d846321163782115c82115db84031
55e1427f85f10a5c9a7755877748041af1bcd8d474ec065eb33df57a97babf54bfd2103575fa8291
15d224c523596b401065a97f74010610fce76382c0bf32f84984010203040101b840312c55512422
cf9b8a4097e9a6ad79402e87a15ae909a4bfefa22398f03d20951933beea1e4dfa6f968212385e82
9f04c2d314fc2d4e255e0d3bc08792b069dbf8599020010db83c4d001500000000abcdef12820d05
820d05b84038643200b172dcfef857492156971f0e6aa2c538d8b74010f8e140811d53b98c765dd2
d96126051913f44582e8c199ad7c6d6819e9a56483f637feaac9448aacf8599020010db885a308d3
13198a2e037073488203e78203e8b8408dcab8618c3253b558d459da53bd8fa68935a719aff8b811
197101a4b2b47dd2d47295286fc00cc081bb542d760717d1bdd6bec2c37cd72eca367d6dd3b9df73
8443b9a355010203b525a138aa34383fec3d2719a0
```

#### RLPx Handshake

In these test vectors, node A initiates a connection with node B.
The values contained in all packets are given below:

```text
Static Key A:    49a7b37aa6f6645917e7b807e9d1c00d4fa71f18343b0d4122a4d2df64dd6fee
Static Key B:    b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291
Ephemeral Key A: 869d6ecf5211f1cc60418a13b9d870b22959d0c16f02bec714c960dd2298a32d
Ephemeral Key B: e238eb8e04fee6511ab04c6dd3c89ce097b11f25d584863ac2b6d5b35b1847e4
Nonce A:         7e968bba13b6c50e2c4cd7f241cc0d64d1ac25c7f5952df231ac6a2bda8ee5d6
Nonce B:         559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd
```

(Auth₁)  RLPx v4 format (sent from A to B):
```text
048ca79ad18e4b0659fab4853fe5bc58eb83992980f4c9cc147d2aa31532efd29a3d3dc6a3d89eaf
913150cfc777ce0ce4af2758bf4810235f6e6ceccfee1acc6b22c005e9e3a49d6448610a58e98744
ba3ac0399e82692d67c1f58849050b3024e21a52c9d3b01d871ff5f210817912773e610443a9ef14
2e91cdba0bd77b5fdf0769b05671fc35f83d83e4d3b0b000c6b2a1b1bba89e0fc51bf4e460df3105
c444f14be226458940d6061c296350937ffd5e3acaceeaaefd3c6f74be8e23e0f45163cc7ebd7622
0f0128410fd05250273156d548a414444ae2f7dea4dfca2d43c057adb701a715bf59f6fb66b2d1d2
0f2c703f851cbf5ac47396d9ca65b6260bd141ac4d53e2de585a73d1750780db4c9ee4cd4d225173
a4592ee77e2bd94d0be3691f3b406f9bba9b591fc63facc016bfa8
```

(Auth₂) EIP-8 format with version 4 and no additional list elements (sent from A to B):
```text
01b304ab7578555167be8154d5cc456f567d5ba302662433674222360f08d5f1534499d3678b513b
0fca474f3a514b18e75683032eb63fccb16c156dc6eb2c0b1593f0d84ac74f6e475f1b8d56116b84
9634a8c458705bf83a626ea0384d4d7341aae591fae42ce6bd5c850bfe0b999a694a49bbbaf3ef6c
da61110601d3b4c02ab6c30437257a6e0117792631a4b47c1d52fc0f8f89caadeb7d02770bf999cc
147d2df3b62e1ffb2c9d8c125a3984865356266bca11ce7d3a688663a51d82defaa8aad69da39ab6
d5470e81ec5f2a7a47fb865ff7cca21516f9299a07b1bc63ba56c7a1a892112841ca44b6e0034dee
70c9adabc15d76a54f443593fafdc3b27af8059703f88928e199cb122362a4b35f62386da7caad09
c001edaeb5f8a06d2b26fb6cb93c52a9fca51853b68193916982358fe1e5369e249875bb8d0d0ec3
6f917bc5e1eafd5896d46bd61ff23f1a863a8a8dcd54c7b109b771c8e61ec9c8908c733c0263440e
2aa067241aaa433f0bb053c7b31a838504b148f570c0ad62837129e547678c5190341e4f1693956c
3bf7678318e2d5b5340c9e488eefea198576344afbdf66db5f51204a6961a63ce072c8926c
```

(Auth₃) EIP-8 format with version 56 and 3 additional list elements (sent from A to B):
```text
01b8044c6c312173685d1edd268aa95e1d495474c6959bcdd10067ba4c9013df9e40ff45f5bfd6f7
2471f93a91b493f8e00abc4b80f682973de715d77ba3a005a242eb859f9a211d93a347fa64b597bf
280a6b88e26299cf263b01b8dfdb712278464fd1c25840b995e84d367d743f66c0e54a586725b7bb
f12acca27170ae3283c1073adda4b6d79f27656993aefccf16e0d0409fe07db2dc398a1b7e8ee93b
cd181485fd332f381d6a050fba4c7641a5112ac1b0b61168d20f01b479e19adf7fdbfa0905f63352
bfc7e23cf3357657455119d879c78d3cf8c8c06375f3f7d4861aa02a122467e069acaf513025ff19
6641f6d2810ce493f51bee9c966b15c5043505350392b57645385a18c78f14669cc4d960446c1757
1b7c5d725021babbcd786957f3d17089c084907bda22c2b2675b4378b114c601d858802a55345a15
116bc61da4193996187ed70d16730e9ae6b3bb8787ebcaea1871d850997ddc08b4f4ea668fbf3740
7ac044b55be0908ecb94d4ed172ece66fd31bfdadf2b97a8bc690163ee11f5b575a4b44e36e2bfb2
f0fce91676fd64c7773bac6a003f481fddd0bae0a1f31aa27504e2a533af4cef3b623f4791b2cca6
d490
```

(Ack₁) RLPx v4 format (sent from B to A):
```text
049f8abcfa9c0dc65b982e98af921bc0ba6e4243169348a236abe9df5f93aa69d99cadddaa387662
b0ff2c08e9006d5a11a278b1b3331e5aaabf0a32f01281b6f4ede0e09a2d5f585b26513cb794d963
5a57563921c04a9090b4f14ee42be1a5461049af4ea7a7f49bf4c97a352d39c8d02ee4acc416388c
1c66cec761d2bc1c72da6ba143477f049c9d2dde846c252c111b904f630ac98e51609b3b1f58168d
dca6505b7196532e5f85b259a20c45e1979491683fee108e9660edbf38f3add489ae73e3dda2c71b
d1497113d5c755e942d1
```

(Ack₂) EIP-8 format with version 4 and no additional list elements (sent from B to A):
```text
01ea0451958701280a56482929d3b0757da8f7fbe5286784beead59d95089c217c9b917788989470
b0e330cc6e4fb383c0340ed85fab836ec9fb8a49672712aeabbdfd1e837c1ff4cace34311cd7f4de
05d59279e3524ab26ef753a0095637ac88f2b499b9914b5f64e143eae548a1066e14cd2f4bd7f814
c4652f11b254f8a2d0191e2f5546fae6055694aed14d906df79ad3b407d94692694e259191cde171
ad542fc588fa2b7333313d82a9f887332f1dfc36cea03f831cb9a23fea05b33deb999e85489e645f
6aab1872475d488d7bd6c7c120caf28dbfc5d6833888155ed69d34dbdc39c1f299be1057810f34fb
e754d021bfca14dc989753d61c413d261934e1a9c67ee060a25eefb54e81a4d14baff922180c395d
3f998d70f46f6b58306f969627ae364497e73fc27f6d17ae45a413d322cb8814276be6ddd13b885b
201b943213656cde498fa0e9ddc8e0b8f8a53824fbd82254f3e2c17e8eaea009c38b4aa0a3f306e8
797db43c25d68e86f262e564086f59a2fc60511c42abfb3057c247a8a8fe4fb3ccbadde17514b7ac
8000cdb6a912778426260c47f38919a91f25f4b5ffb455d6aaaf150f7e5529c100ce62d6d92826a7
1778d809bdf60232ae21ce8a437eca8223f45ac37f6487452ce626f549b3b5fdee26afd2072e4bc7
5833c2464c805246155289f4
```

(Ack₃) EIP-8 format with version 57 and 3 additional list elements (sent from B to A):
```text
01f004076e58aae772bb101ab1a8e64e01ee96e64857ce82b1113817c6cdd52c09d26f7b90981cd7
ae835aeac72e1573b8a0225dd56d157a010846d888dac7464baf53f2ad4e3d584531fa203658fab0
3a06c9fd5e35737e417bc28c1cbf5e5dfc666de7090f69c3b29754725f84f75382891c561040ea1d
dc0d8f381ed1b9d0d4ad2a0ec021421d847820d6fa0ba66eaf58175f1b235e851c7e2124069fbc20
2888ddb3ac4d56bcbd1b9b7eab59e78f2e2d400905050f4a92dec1c4bdf797b3fc9b2f8e84a482f3
d800386186712dae00d5c386ec9387a5e9c9a1aca5a573ca91082c7d68421f388e79127a5177d4f8
590237364fd348c9611fa39f78dcdceee3f390f07991b7b47e1daa3ebcb6ccc9607811cb17ce51f1
c8c2c5098dbdd28fca547b3f58c01a424ac05f869f49c6a34672ea2cbbc558428aa1fe48bbfd6115
8b1b735a65d99f21e70dbc020bfdface9f724a0d1fb5895db971cc81aa7608baa0920abb0a565c9c
436e2fd13323428296c86385f2384e408a31e104670df0791d93e743a3a5194ee6b076fb6323ca59
3011b7348c16cf58f66b9633906ba54a2ee803187344b394f75dd2e663a57b956cb830dd7a908d4f
39a2336a61ef9fda549180d4ccde21514d117b6c6fd07a9102b5efe710a32af4eeacae2cb3b1dec0
35b9593b48b9d3ca4c13d245d5f04169b0b1
```

Node B derives the connection secrets for (Auth₂, Ack₂) as follows:

```text
aes-secret = 80e8632c05fed6fc2a13b0f8d31a3cf645366239170ea067065aba8e28bac487
mac-secret = 2ea74ec5dae199227dff1af715362700e989d889d7a493cb0639691efb8e5f98
```

Running B's `ingress-mac` keccak state on the string "foo" yields the hash

```text
ingress-mac("foo") = 0c7ec6340062cc46f5e9f1e3cf86f8c8c403c5a0964f5df0ebd34a75ddc86db5
```


#master_eips.md
#eip-1.md
    EIP: 1
      Title: EIP Purpose and Guidelines
      Status: Draft
      Type: Meta
      Author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>
      Created: 2015-10-27, 2017-02-01

What is an EIP?
--------------

EIP stands for Ethereum Improvement Proposal. An EIP is a design document providing information to the Ethereum community, or describing a new feature for Ethereum or its processes or environment. The EIP should provide a concise technical specification of the feature and a rationale for the feature. The EIP author is responsible for building consensus within the community and documenting dissenting opinions.

EIP Rational
------------

We intend EIPs to be the primary mechanisms for proposing new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Ethereum. Because the EIPs are maintained as text files in a versioned repository, their revision history is the historical record of the feature proposal.

For Ethereum implementers, EIPs are a convenient way to track the progress of their implementation. Ideally each implementation maintainer would list the EIPs that they have implemented. This will give end users a convenient way to know the current status of a given implementation or library.

EIP Types
---------

There are three types of EIP:

-   A **Standard Track EIP** describes any change that affects most or all Ethereum implementations, such as a change to the the network protocol, a change in block or transaction validity rules, proposed application standards/conventions, or any change or addition that affects the interoperability of applications using Ethereum. Furthermore Standard EIPs can be broken down into the following categories.
    -   **Core** - improvements requiring a consensus fork (e.g. [EIP5], [EIP101]), as well as changes that are not necessarily consensus critical but may be relevant to “core dev” discussions (for example, [EIP90], and the miner/node strategy changes 2, 3, and 4 of [EIP86]).
    -   **Networking** - includes improvements around [devp2p] ([EIP8]) and [Light Ethereum Subprotocol], as well as proposed improvements to network protocol specifications of [whisper] and [swarm].
    -   **Interface** - includes improvements around client [API/RPC] specifications and standards, and also certain language-level standards like method names ([EIP59], [EIP6]) and [contract ABIs]. The label “interface” aligns with the [interfaces repo] and discussion should primarily occur in that repository before an EIP is submitted to the EIPs repository.
    -   **ERC** - application-level standards and conventions, including contract standards such as token standards ([ERC20]), name registries ([ERC26], [ERC137]), URI schemes ([ERC67]), library/package formats ([EIP82]), and wallet formats ([EIP75], [EIP85]).

-   An **Informational EIP** describes a Ethereum design issue, or provides general guidelines or information to the Ethereum community, but does not propose a new feature. Informational EIPs do not necessarily represent Ethereum community consensus or a recommendation, so users and implementers are free to ignore Informational EIPs or follow their advice.
-   A **Meta EIP** describes a process surrounding Ethereum or proposes a change to (or an event in) a process. Process EIPs are like Standards Track EIPs but apply to areas other than the Ethereum protocol itself. They may propose an implementation, but not to Ethereum's codebase; they often require community consensus; unlike Informational EIPs, they are more than recommendations, and users are typically not free to ignore them. Examples include procedures, guidelines, changes to the decision-making process, and changes to the tools or environment used in Ethereum development. Any meta-EIP is also considered a Process EIP.

EIP Work Flow
-------------

The EIP repository Collaborators change the EIPs status. Please send all EIP-related email to the EIP Collaborators, which is listed under EIP Editors below. Also see EIP Editor Responsibilities & Workflow.

The EIP process begins with a new idea for Ethereum. It is highly recommended that a single EIP contain a single key proposal or new idea. The more focused the EIP, the more successful it tends to be. A change to one client doesn't require an EIP; a change that affects multiple clients, or defines a standard for multiple apps to use, does. The EIP editor reserves the right to reject EIP proposals if they appear too unfocused or too broad. If in doubt, split your EIP into several well-focused ones.

Each EIP must have a champion - someone who writes the EIP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea.

Vetting an idea publicly before going as far as writing an EIP is meant to save the potential author time. Asking the Ethereum community first if an idea is original helps prevent too much time being spent on something that is guaranteed to be rejected based on prior discussions (searching the Internet does not always do the trick). It also helps to make sure the idea is applicable to the entire community and not just the author. Just because an idea sounds good to the author does not mean it will work for most people in most areas where Ethereum is used. Examples of appropriate public forums to gauge interest around your EIP include [the Ethereum subreddit], [the Issues section of this repository], and [one of the Ethereum Gitter chat rooms]. In particular, [the Issues section of this repository] is an excellent place to discuss your proposal with the community and start creating more formalized language around your EIP. 

Once the champion has asked the Ethereum community whether an idea has any chance of acceptance a draft EIP should be presented as a [pull request]. This gives the author a chance to continuously edit the draft EIP for proper formatting and quality. This also allows for further public comment and the author of the EIP to address concerns about the proposal.

If the EIP collaborators approve, the EIP editor will assign the EIP a number (generally the issue or PR number related to the EIP), label it as Standards Track, Informational, or Meta, give it status “Draft”, and add it to the git repository. The EIP editor will not unreasonably deny an EIP. Reasons for denying EIP status include duplication of effort, being technically unsound, not providing proper motivation or addressing backwards compatibility, or not in keeping with the Ethereum philosophy.

Standards Track EIPs consist of three parts, a design document, implementation, and finally if warranted an update to the [formal specification]. The EIP should be reviewed and accepted before an implementation is begun, unless an implementation will aid people in studying the EIP. Standards Track EIPs must be implemented in at least three viable Ethereum clients before it can be considered Final.

For an EIP to be accepted it must meet certain minimum criteria. It must be a clear and complete description of the proposed enhancement. The enhancement must represent a net improvement. The proposed implementation, if applicable, must be solid and must not complicate the protocol unduly.

Once an EIP has been accepted, the implementations must be completed. When the implementation is complete and accepted by the community, the status will be changed to “Final”.

An EIP can also be assigned status “Deferred”. The EIP author or editor can assign the EIP this status when no progress is being made on the EIP. Once an EIP is deferred, the EIP editor can re-assign it to draft status.

An EIP can also be “Rejected”. Perhaps after all is said and done it was not a good idea. It is still important to have a record of this fact.

EIPs can also be superseded by a different EIP, rendering the original obsolete.

The possible paths of the status of EIPs are as follows:

<img src=./eip-1/process.png>

Some Informational and Process EIPs may also have a status of “Active” if they are never meant to be completed. E.g. EIP 1 (this EIP).

What belongs in a successful EIP?
---------------------------------

Each EIP should have the following parts:

-   Preamble - RFC 822 style headers containing metadata about the EIP, including the EIP number, a short descriptive title (limited to a maximum of 44 characters), the names, and optionally the contact info for each author, etc.

<!-- -->

-   Simple Summary - “If you can’t explain it simply, you don’t understand it well enough.” Provide a simplified and layman-accessible explanation of the EIP.

<!-- -->

-   Abstract - a short (~200 word) description of the technical issue being addressed.

<!-- -->

-   Motivation (*optional) - The motivation is critical for EIPs that want to change the Ethereum protocol. It should clearly explain why the existing protocol specification is inadequate to address the problem that the EIP solves. EIP submissions without sufficient motivation may be rejected outright.

<!-- -->

-   Specification - The technical specification should describe the syntax and semantics of any new feature. The specification should be detailed enough to allow competing, interoperable implementations for any of the current Ethereum platforms (cpp-ethereum, go-ethereum, parity, ethereumJ, ethereumjs-lib, …).

<!-- -->

-   Rationale - The rationale fleshes out the specification by describing what motivated the design and why particular design decisions were made. It should describe alternate designs that were considered and related work, e.g. how the feature is supported in other languages. The rationale may also provide evidence of consensus within the community, and should discuss important objections or concerns raised during discussion.

<!-- -->

-   Backwards Compatibility - All EIPs that introduce backwards incompatibilities must include a section describing these incompatibilities and their severity. The EIP must explain how the author proposes to deal with these incompatibilities. EIP submissions without a sufficient backwards compatibility treatise may be rejected outright.

<!-- -->

-   Test Cases - Test cases for an implementation are mandatory for EIPs that are affecting consensus changes. Other EIPs can choose to include links to test cases if applicable.

<!-- -->

-   Implementations - The implementations must be completed before any EIP is given status “Final”, but it need not be completed before the EIP is accepted. While there is merit to the approach of reaching consensus on the specification and rationale before writing code, the principle of “rough consensus and running code” is still useful when it comes to resolving many discussions of API details.

EIP Formats and Templates
-------------------------

EIPs should be written in [markdown] format. Image files should be included in a subdirectory for that EIP.

EIP Header Preamble
-------------------

Each EIP must begin with an RFC 822 style header preamble. The headers must appear in the following order. Headers marked with "*" are optional and are described below. All other headers are required.

` EIP: ` <EIP number> (this is determined by the EIP editor)

` Title: `<EIP title>

` Author: `<list of author's real names and optionally, email address>

` * Discussions-To: ` <email address>

` Status: `<Draft | Active | Accepted | Deferred | Rejected | Withdrawn | Final | Superseded>

` Type: `<Standards Track (Core, Networking, Interface, ERC)  | Informational | Process>

` Created: `<date created on, in ISO 8601 (yyyy-mm-dd) format>

` * Replaces: `<EIP number>

` * Superseded-By: `<EIP number>

` * Resolution: `<url>

The Author header lists the names, and optionally the email addresses of all the authors/owners of the EIP. The format of the Author header value must be

Random J. User &lt;address@dom.ain&gt;

if the email address is included, and

Random J. User

if the email address is not given.

Note: The Resolution header is required for Standards Track EIPs only. It contains a URL that should point to an email message or other web resource where the pronouncement about the EIP is made.

While an EIP is in private discussions (usually during the initial Draft phase), a Discussions-To header will indicate the mailing list or URL where the EIP is being discussed. No Discussions-To header is necessary if the EIP is being discussed privately with the author.

The Type header specifies the type of EIP: Standards Track, Meta, or Informational. If the track is Standards please include the subcategory (core, networking, interface, or ERC).

The Created header records the date that the EIP was assigned a number. Both headers should be in yyyy-mm-dd format, e.g. 2001-08-14.

EIPs may have a Requires header, indicating the EIP numbers that this EIP depends on.

EIPs may also have a Superseded-By header indicating that an EIP has been rendered obsolete by a later document; the value is the number of the EIP that replaces the current document. The newer EIP must have a Replaces header containing the number of the EIP that it rendered obsolete.

Auxiliary Files
---------------

EIPs may include auxiliary files such as diagrams. Such files must be named EIP-XXXX-Y.ext, where “XXXX” is the EIP number, “Y” is a serial number (starting at 1), and “ext” is replaced by the actual file extension (e.g. “png”).

Transferring EIP Ownership
--------------------------

It occasionally becomes necessary to transfer ownership of EIPs to a new champion. In general, we'd like to retain the original author as a co-author of the transferred EIP, but that's really up to the original author. A good reason to transfer ownership is because the original author no longer has the time or interest in updating it or following through with the EIP process, or has fallen off the face of the 'net (i.e. is unreachable or not responding to email). A bad reason to transfer ownership is because you don't agree with the direction of the EIP. We try to build consensus around an EIP, but if that's not possible, you can always submit a competing EIP.

If you are interested in assuming ownership of an EIP, send a message asking to take over, addressed to both the original author and the EIP editor. If the original author doesn't respond to email in a timely manner, the EIP editor will make a unilateral decision (it's not like such decisions can't be reversed :).

EIP Editors
-----------

The current EIP editors are

` * Casey Detrio (@cdetrio)`

` * Fabian Vogelsteller (@frozeman)`

` * Gavin Wood (@gavofyork)`

` * Hudson Jameson (@Souptacular)`

` * Jeffrey Wilcke (@obscuren)`

` * Martin Becze (@wanderer)`

` * Nick Johnson (@arachnid)`

` * Roman Mandeleil (@romanman)`

` * Vitalik Buterin (@vbuterin)`

EIP Editor Responsibilities and Workflow
--------------------------------------

For each new EIP that comes in, an editor does the following:

-   Read the EIP to check if it is ready: sound and complete. The ideas must make technical sense, even if they don't seem likely to be accepted.
-   The title should accurately describe the content.
-   Edit the EIP for language (spelling, grammar, sentence structure, etc.), markup (Github flavored Markdown), code style

If the EIP isn't ready, the editor will send it back to the author for revision, with specific instructions.

Once the EIP is ready for the repository, the EIP editor will:

-   Assign an EIP number (generally the PR number or, if preferred by the author, the Issue # if there was discussion in the Issues section of this repository about this EIP)

<!-- -->

-   Accept the corresponding pull request

<!-- -->

-   List the EIP in [README.md]

<!-- -->

-   Send a message back to the EIP author with next step.

Many EIPs are written and maintained by developers with write access to the Ethereum codebase. The EIP editors monitor EIP changes, and correct any structure, grammar, spelling, or markup mistakes we see.

The editors don't pass judgment on EIPs. We merely do the administrative & editorial part.

History
-------

This document was derived heavily from [Bitcoin's BIP-0001] written by Amir Taaki which in turn was derived from [Python's PEP-0001]. In many places text was simply copied and modified. Although the PEP-0001 text was written by Barry Warsaw, Jeremy Hylton, and David Goodger, they are not responsible for its use in the Ethereum Improvement Process, and should not be bothered with technical questions specific to Ethereum or the EIP. Please direct all comments to the EIP editors.

December 7, 2016: EIP 1 has been improved and will be placed as a PR.

February 1, 2016: EIP 1 has added editors, made draft improvements to process, and has merged with Master stream.

  [EIP5]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-5.md
  [EIP101]: https://github.com/ethereum/EIPs/issues/28
  [EIP90]: https://github.com/ethereum/EIPs/issues/90
  [EIP86]: https://github.com/ethereum/EIPs/issues/86#issue-145324865
  [devp2p]: https://github.com/ethereum/wiki/wiki/%C3%90%CE%9EVp2p-Wire-Protocol
  [EIP8]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8.md
  [Light Ethereum Subprotocol]: https://github.com/ethereum/wiki/wiki/Light-client-protocol
  [whisper]: https://gist.github.com/gluk256/4654922ca45eb9d0846d941d7ca326f4
  [swarm]: https://github.com/ethereum/go-ethereum/pull/2959
  [API/RPC]: https://github.com/ethereum/wiki/wiki/JSON-RPC
  [EIP59]: https://github.com/ethereum/EIPs/issues/59
  [EIP6]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-6.md
  [contract ABIs]: https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI
  [interfaces repo]: https://github.com/ethereum/interfaces
  [ERC20]: https://github.com/ethereum/EIPs/issues/20
  [ERC26]: https://github.com/ethereum/EIPs/issues/26
  [ERC137]: https://github.com/ethereum/EIPs/issues/137
  [ERC67]: https://github.com/ethereum/EIPs/issues/67
  [EIP82]: https://github.com/ethereum/EIPs/issues/82
  [EIP75]: https://github.com/ethereum/EIPs/issues/75
  [EIP85]: https://github.com/ethereum/EIPs/issues/85
  [the Ethereum subreddit]: https://www.reddit.com/r/ethereum/
  [one of the Ethereum Gitter chat rooms]: https://gitter.im/ethereum/
  [pull request]: https://github.com/ethereum/EIPs/pulls
  [formal specification]: https://github.com/ethereum/yellowpaper
  [the Issues section of this repository]: https://github.com/ethereum/EIPs/issues
  [markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
  [README.md]: README.md "wikilink"
  [Bitcoin's BIP-0001]: https://github.com/bitcoin/bips
  [Python's PEP-0001]: https://www.python.org/dev/peps/


#eip-101.md
### Title

      EIP: 101
      Title: Serenity Currency and Crypto Abstraction
      Author: Vitalik Buterin <v@buterin.com>
      Status: Active
      Type: Serenity feature
      Created: 2015-11-15

### Specification

1.  Accounts now have only two fields in their RLP encoding: **code** and **storage**.
2.  Ether is no longer stored in account objects directly; instead, at address `0`, we premine a contract which contains all ether holdings. The `eth.getBalance` command in web3 is remapped appropriately.
3.  `msg.value` no longer exists as an opcode.
4.  A transaction now only has four fields: **to**, **startgas**, **data** and **code**.
5.  Aside from an RLP validity check, and checking that the **to** field is twenty bytes long, the **startgas** is an integer, and **code** is either empty or hashes to the **to** address, there are no other validity constraints; anything goes. However, the block gas limit remains, so miners are disincentivized from including junk.
6.  Gas is charged for bytes in **code** at the same rate as **data**.
7.  When a transaction is sent, if the receiving account does not yet exist, the account is created, and its code is set to the code provided in the transaction; otherwise the code is ignored.
8.  A `tx.gas` opcode is added alongside the existing `msg.gas` at index `0x5c`; this new opcode allows the transaction to access the original amount of gas allotted for the transaction

Note that `ECRECOVER`, sequence number/nonce incrementing and ether are now nowhere in the bottom-level spec (NOTE: ether is going to continue to have a privileged role in Casper PoS). To replicate existing functionality under the new model, we do the following.

Simple user accounts can have the following default standardized code:

```python
# We assume that data takes the following schema:
# bytes 0-31: v (ECDSA sig)
# bytes 32-63: r (ECDSA sig)
# bytes 64-95: s (ECDSA sig)
# bytes 96-127: sequence number (formerly called "nonce")
# bytes 128-159: gasprice
# bytes 172-191: to
# bytes 192+: data

# Get the hash for transaction signing
~mstore(0, msg.gas)
~calldatacopy(32, 96, ~calldatasize() - 96)
h = sha3(96, ~calldatasize() - 96)
# Call ECRECOVER contract to get the sender
~call(5000, 3, [h, ~calldataload(0), ~calldataload(32), ~calldataload(64)], 128, ref(addr), 32)
# Check sender correctness
assert addr == 0x82a978b3f5962a5b0957d9ee9eef472ee55b42f1
# Check sequence number correctness
assert ~calldataload(96) == self.storage[-1]
# Increment sequence number
self.storage[-1] += 1
# Make the sub-call and discard output
~call(msg.gas - 50000, ~calldataload(160), 192, ~calldatasize() - 192, 0, 0)
# Pay for gas
~call(40000, 0, [SEND, block.coinbase, ~calldataload(128) * (tx.gas - msg.gas + 50000)], 96, 0, 0)
```

This essentially implements signature and nonce checking, and if both checks pass then it uses all remaining gas minus 50000 to send the actual desired call, and then finally pays for gas.

Miners can follow the following algorithm upon receiving transactions:

1.  Run the code for a maximum of 50000 gas, stopping if they see an operation or call that threatens to go over this limit
2.  Upon seeing that operation, make sure that it leaves at last 50000 gas to spare (either by checking that the static gas consumption is small enough or by checking that it is a call with `msg.gas - 50000` as its gas limit parameter)
3.  Pattern-match to make sure that gas payment code at the end is *exactly* the same as in the code above.

This process ensures that miners *waste* at most 50000 gas before knowing whether or not it will be worth their while to include the transaction, and is also highly general so users can experiment with new cryptography (eg. ed25519, Lamport), ring signatures, quasi-native multisig, etc. Theoretically, one can even create an account for which the *valid signature* type is a valid Merkle branch of a receipt, creating a quasi-native alarm clock.

If someone wants to send a transaction with nonzero value, instead of the current `msg.sender` approach, we compile into a three step process:

1.  In the outer scope just before calling, call the ether contract to create a cheque for the desired amount
2.  In the inner scope, if a contract uses the `msg.value` opcode anywhere in the function that is being called, then we have the contract cash out the cheque at the start of the function call and store the amount cashed out in a standardized address in memory
3.  In the outer scope just after calling, send a message to the ether contract to disable the cheque if it has not yet been cashed

### Rationale

This allows for a large increase in generality, particularly in a few
areas:

1.  Cryptographic algorithms used to secure accounts (we could reasonably say that Ethereum is quantum-safe, as one is perfectly free to secure one's account with Lamport signatures). The nonce-incrementing approach is now also open to revision on the part of account holders, allowing for experimentation in k-parallelizable nonce techniques, UTXO schemes, etc.
2.  Moving ether up a level of abstraction, with the particular benefit of allowing ether and sub-tokens to be treated similarly by contracts
3.  Reducing the level of indirection required for custom-policy accounts such as multisigs

It also substantially simplifies and *purifies* the underlying Ethereum protocol, reducing the minimal consensus implementation complexity.

### Implementation

Coming soon.


#eip-107.md
<pre>
  EIP: 107
  Title: safe "eth_sendTransaction" authorization via html popup
  Author: Ronan Sandford <wighawag@gmail.com>
  Created: 2016-06-05
  Status: Draft
  Type: Standard
  Category: Interface
</pre>

Abstract
========
This draft EIP describes the details of an authorization method that if provided by rpc enabled ethereum nodes would allow regular websites to send transactions (via ```eth_sendTransaction```) without the need to enable CORS. Instead, user would be asked to confirm the transaction via an html popup. 

Every read only rpc call the dapp wants to perform is redirected to an invisible iframe from the node's domain and for every transaction that the dapp wish to execute, an html popup is presented to the user to allow him/her to cancel or confirm the transaction. This allows the dapp to connect to the node's rpc api without being  granted any kind of privileges. This allows users to safely interact with dapps running in their everyday web browser while their accounts are unlocked. In case the account is not unlocked, and the node has allowed the "personal" api via rpc,the html page also allow the user to enter their password to unlock the account for the scope of the transaction.

Motivation
==========
Currently, if a user navigates to a dapp running on a website using her/his everyday browser, the dapp will by default have no access to the rpc api for security reasons. The user will have to enable CORS for the website's domain in order for the dapp to work. Unfortunately if the user does so, the dapp will be able to send transactions from any unlocked account without the need for any user consent. In other words, not only does the user need to change the node's default setting, but the user is also forced to trust the dapp in order to use it. This is of course not acceptable and forces existing dapps to rely on the use of workarrounds like:
- if the transaction is a plain ether transfer, the user is asked to enter it in a dedicated trusted wallet like "Mist"
- For more complex case, the user is asked to enter the transaction manually via the node command line interface.


This proposal aims to provide a safe and user friendly alternative.

Here are some screenshots of the provided implementation of that html popup:

Account unlocked :
-----------------
When the account is already unlocked, the user is presented with the following popup for every transaction that the dapp attempts to make:

<img src="./eip-107/authorization.png">

Account locked and no "personal" api exposed via rpc:
-----------------
When the account is locked, and the node does not provide access to account unlocking via its rpc interface, the following popup will be presented. This is not ideal since this requires the user to know how to unlock an account:

<img src="./eip-107/authorization-locked.png">

Account locked but node exposing the "personal" api via rpc :
-----------------
A better option is to ask the user for their password, but this is only possible if the node allows access to the "personal" api via rpc. In such case, the following dialog will be presented to the user so he/she can accept the transaction by providing the password required to unlock the account:

<img src="./eip-107/authorization-password.png">


Specification
=============
In order for the mechanism to work, the node needs to serve an html file via http at the url \<node url\>/authorization.html

This file will then be used by the dapp in 2 different modes (invisible iframe and popup window).

The invisible iframe will be embeded in the dapp to allow the dapp to send its read-only rpc call without having to enable CORS for the dapp's website domain. This is done by sending message to the iframe (via javascript ```window.postMessage```) which in turn execute the rpc call. This works since the iframe and the node share the same domain/port. 

In the iframe mode, the html file's javascript code will ensure that no call requiring an unlocked key can be made. This is to prevent dapps from embedding the invisible iframe and tricking the user into clicking the confirm button.
If the dapp requires an ```eth_sendTransaction``` call, the dapp will instead open a new window using the same url.

In this popup window mode, the html file's javascript code will alow ```eth_sendTransaction``` (but not  ```eth_sign```, as there is no way to display to the user the meaningful content of the transaction to sign in a safe way) to be called. But instead of sending the call to the node directly, a confirmation dialog will be presented showing the sender and recipient addresses, as well as the amount being transfered along with the potential gas cost. Upon the user approving, the request will be sent and the result returned to the dapp. An error will be returned in case the user cancel the request. 

The html page also checks for the availability of the "personal" api and if so, will ask the user to unlock the account if necessary. The unlocking is temporary (3s) so the password will be asked again if a transaction is attempted before the end of this short time.

In both iframe mode and window mode, the communication with the dapp is achieved using ```window.postMessage```. 
The fist message the iframe/window sends is a message containing the string "ready" to let the dapp know that it now accepts messages. Then the dapp can start performing rpc call by sending message using the following object :
```
{
  id:<a an id>, //so responses can be match as there is no guarantee of the order of the response
  payload:<json rpc object> //this is the exact object that usually send to the node
}
```

For ```eth_sendTransaction``` the "gas", "gasPrice" and "from" field need to be set in the rpc parameter so that the window can display the correct value. If not all of these are passed in, the window will return an error.

Upon receiving such message, the iframe will perform the actual rpc call to the node but only if such a call is a read only call (not requiring an unlocked key). If it is not it will return a error. The window on the other will only accept ```eth_sendTransaction``` calls but will display a dialog so the user can accept or cancel the request.

In all the cases, the iframe/window will send a message back to the dapp using the following object:
```
{
  id:<id matchign the request>,
  result:<rpc result as is>,
  error:<error object>
}
```

the error object cannot be a javascript Error object due to postMessage limitation. Instead it is 
```
{
  message:<a string describing the error>,
  type:<a string defining the type of error> //type="cancel" means the user cancel the transaction
}
```


Rationale
=========
The design for that proposal was chosen for its simplicity and security. A previous idea was to use an oauth-like protocol in order for the user to accept or deny a transaction request. It would have required deeper code change in the node and some geth contributors argues that such change did not fit into geth code base as it would have required dapp aware code. 
The current design, instead has a very simple implementation (self contained html file that can be shared across node's implementation) and its safeness is guarantess by browsers' cross domain policies.

The use of iframe/ window was required to have both security and user friendliness. The invisble iframe allows the dapp to execute read only calls without the need for user input, and the window ensures user approval before making a call. While we could have made it without the window mode by making the iframe confirmation use the native browser ```window.confirm``` dialog, this would have prevented the use of a more elegant confirmation popup that the current design allows. It also happens to be that the ```window.confirm``` is not safe in some browsers, as it gives focus to the accept option and can be triggered automatically (https://bugs.chromium.org/p/chromium/issues/detail?id=260653).


Implementations
===============
In order to implement this design, the following html file or an equivalent one needs to be served at the url \<node url\>/authorization.html

That's it.


```
<!DOCTYPE html>
<html>
  <head>
    <title>Ethereum Authorization</title>
  </head>
  <script>
    //https://github.com/alexvandesande/blockies
    !function(){function r(r){for(var t=0;t<l.length;t++)l[t]=0;for(var t=0;t<r.length;t++)l[t%4]=(l[t%4]<<5)-l[t%4]+r.charCodeAt(t)}function t(){var r=l[0]^l[0]<<11;return l[0]=l[1],l[1]=l[2],l[2]=l[3],l[3]=l[3]^l[3]>>19^r^r>>8,(l[3]>>>0)/(1<<31>>>0)}function e(){var r=Math.floor(360*t()),e=60*t()+40+"%",o=25*(t()+t()+t()+t())+"%",n="hsl("+r+","+e+","+o+")";return n}function o(r){for(var e=r,o=r,n=Math.ceil(e/2),a=e-n,l=[],c=0;o>c;c++){for(var f=[],h=0;n>h;h++)f[h]=Math.floor(2.3*t());var i=f.slice(0,a);i.reverse(),f=f.concat(i);for(var v=0;v<f.length;v++)l.push(f[v])}return l}function n(r,t,e,o,n){var a=document.createElement("canvas"),l=Math.sqrt(r.length);a.width=a.height=l*e;var c=a.getContext("2d");c.fillStyle=o,c.fillRect(0,0,a.width,a.height),c.fillStyle=t;for(var f=0;f<r.length;f++){var h=Math.floor(f/l),i=f%l;c.fillStyle=1==r[f]?t:n,r[f]&&c.fillRect(i*e,h*e,e,e)}return a}function a(t){t=t||{};var a=t.size||8,l=t.scale||4,c=t.seed||Math.floor(Math.random()*Math.pow(10,16)).toString(16);r(c);var f=t.color||e(),h=t.bgcolor||e(),i=t.spotcolor||e(),v=o(a),u=n(v,f,l,h,i);return u}var l=new Array(4);window.blockies={create:a}}();
    
    /* bignumber.js v2.3.0 https://github.com/MikeMcl/bignumber.js/LICENCE */
    !function(e){"use strict";function n(e){function E(e,n){var t,r,i,o,u,s,f=this;if(!(f instanceof E))return j&&L(26,"constructor call without new",e),new E(e,n);if(null!=n&&H(n,2,64,M,"base")){if(n=0|n,s=e+"",10==n)return f=new E(e instanceof E?e:s),U(f,P+f.e+1,k);if((o="number"==typeof e)&&0*e!=0||!new RegExp("^-?"+(t="["+N.slice(0,n)+"]+")+"(?:\\."+t+")?$",37>n?"i":"").test(s))return h(f,s,o,n);o?(f.s=0>1/e?(s=s.slice(1),-1):1,j&&s.replace(/^0\.0*|\./,"").length>15&&L(M,v,e),o=!1):f.s=45===s.charCodeAt(0)?(s=s.slice(1),-1):1,s=D(s,10,n,f.s)}else{if(e instanceof E)return f.s=e.s,f.e=e.e,f.c=(e=e.c)?e.slice():e,void(M=0);if((o="number"==typeof e)&&0*e==0){if(f.s=0>1/e?(e=-e,-1):1,e===~~e){for(r=0,i=e;i>=10;i/=10,r++);return f.e=r,f.c=[e],void(M=0)}s=e+""}else{if(!g.test(s=e+""))return h(f,s,o);f.s=45===s.charCodeAt(0)?(s=s.slice(1),-1):1}}for((r=s.indexOf("."))>-1&&(s=s.replace(".","")),(i=s.search(/e/i))>0?(0>r&&(r=i),r+=+s.slice(i+1),s=s.substring(0,i)):0>r&&(r=s.length),i=0;48===s.charCodeAt(i);i++);for(u=s.length;48===s.charCodeAt(--u););if(s=s.slice(i,u+1))if(u=s.length,o&&j&&u>15&&(e>y||e!==d(e))&&L(M,v,f.s*e),r=r-i-1,r>z)f.c=f.e=null;else if(G>r)f.c=[f.e=0];else{if(f.e=r,f.c=[],i=(r+1)%O,0>r&&(i+=O),u>i){for(i&&f.c.push(+s.slice(0,i)),u-=O;u>i;)f.c.push(+s.slice(i,i+=O));s=s.slice(i),i=O-s.length}else i-=u;for(;i--;s+="0");f.c.push(+s)}else f.c=[f.e=0];M=0}function D(e,n,t,i){var o,u,f,c,a,h,g,p=e.indexOf("."),d=P,m=k;for(37>t&&(e=e.toLowerCase()),p>=0&&(f=J,J=0,e=e.replace(".",""),g=new E(t),a=g.pow(e.length-p),J=f,g.c=s(l(r(a.c),a.e),10,n),g.e=g.c.length),h=s(e,t,n),u=f=h.length;0==h[--f];h.pop());if(!h[0])return"0";if(0>p?--u:(a.c=h,a.e=u,a.s=i,a=C(a,g,d,m,n),h=a.c,c=a.r,u=a.e),o=u+d+1,p=h[o],f=n/2,c=c||0>o||null!=h[o+1],c=4>m?(null!=p||c)&&(0==m||m==(a.s<0?3:2)):p>f||p==f&&(4==m||c||6==m&&1&h[o-1]||m==(a.s<0?8:7)),1>o||!h[0])e=c?l("1",-d):"0";else{if(h.length=o,c)for(--n;++h[--o]>n;)h[o]=0,o||(++u,h.unshift(1));for(f=h.length;!h[--f];);for(p=0,e="";f>=p;e+=N.charAt(h[p++]));e=l(e,u)}return e}function F(e,n,t,i){var o,u,s,c,a;if(t=null!=t&&H(t,0,8,i,w)?0|t:k,!e.c)return e.toString();if(o=e.c[0],s=e.e,null==n)a=r(e.c),a=19==i||24==i&&B>=s?f(a,s):l(a,s);else if(e=U(new E(e),n,t),u=e.e,a=r(e.c),c=a.length,19==i||24==i&&(u>=n||B>=u)){for(;n>c;a+="0",c++);a=f(a,u)}else if(n-=s,a=l(a,u),u+1>c){if(--n>0)for(a+=".";n--;a+="0");}else if(n+=u-c,n>0)for(u+1==c&&(a+=".");n--;a+="0");return e.s<0&&o?"-"+a:a}function _(e,n){var t,r,i=0;for(u(e[0])&&(e=e[0]),t=new E(e[0]);++i<e.length;){if(r=new E(e[i]),!r.s){t=r;break}n.call(t,r)&&(t=r)}return t}function x(e,n,t,r,i){return(n>e||e>t||e!=c(e))&&L(r,(i||"decimal places")+(n>e||e>t?" out of range":" not an integer"),e),!0}function I(e,n,t){for(var r=1,i=n.length;!n[--i];n.pop());for(i=n[0];i>=10;i/=10,r++);return(t=r+t*O-1)>z?e.c=e.e=null:G>t?e.c=[e.e=0]:(e.e=t,e.c=n),e}function L(e,n,t){var r=new Error(["new BigNumber","cmp","config","div","divToInt","eq","gt","gte","lt","lte","minus","mod","plus","precision","random","round","shift","times","toDigits","toExponential","toFixed","toFormat","toFraction","pow","toPrecision","toString","BigNumber"][e]+"() "+n+": "+t);throw r.name="BigNumber Error",M=0,r}function U(e,n,t,r){var i,o,u,s,f,l,c,a=e.c,h=S;if(a){e:{for(i=1,s=a[0];s>=10;s/=10,i++);if(o=n-i,0>o)o+=O,u=n,f=a[l=0],c=f/h[i-u-1]%10|0;else if(l=p((o+1)/O),l>=a.length){if(!r)break e;for(;a.length<=l;a.push(0));f=c=0,i=1,o%=O,u=o-O+1}else{for(f=s=a[l],i=1;s>=10;s/=10,i++);o%=O,u=o-O+i,c=0>u?0:f/h[i-u-1]%10|0}if(r=r||0>n||null!=a[l+1]||(0>u?f:f%h[i-u-1]),r=4>t?(c||r)&&(0==t||t==(e.s<0?3:2)):c>5||5==c&&(4==t||r||6==t&&(o>0?u>0?f/h[i-u]:0:a[l-1])%10&1||t==(e.s<0?8:7)),1>n||!a[0])return a.length=0,r?(n-=e.e+1,a[0]=h[(O-n%O)%O],e.e=-n||0):a[0]=e.e=0,e;if(0==o?(a.length=l,s=1,l--):(a.length=l+1,s=h[O-o],a[l]=u>0?d(f/h[i-u]%h[u])*s:0),r)for(;;){if(0==l){for(o=1,u=a[0];u>=10;u/=10,o++);for(u=a[0]+=s,s=1;u>=10;u/=10,s++);o!=s&&(e.e++,a[0]==b&&(a[0]=1));break}if(a[l]+=s,a[l]!=b)break;a[l--]=0,s=1}for(o=a.length;0===a[--o];a.pop());}e.e>z?e.c=e.e=null:e.e<G&&(e.c=[e.e=0])}return e}var C,M=0,T=E.prototype,q=new E(1),P=20,k=4,B=-7,$=21,G=-1e7,z=1e7,j=!0,H=x,V=!1,W=1,J=100,X={decimalSeparator:".",groupSeparator:",",groupSize:3,secondaryGroupSize:0,fractionGroupSeparator:" ",fractionGroupSize:0};return E.another=n,E.ROUND_UP=0,E.ROUND_DOWN=1,E.ROUND_CEIL=2,E.ROUND_FLOOR=3,E.ROUND_HALF_UP=4,E.ROUND_HALF_DOWN=5,E.ROUND_HALF_EVEN=6,E.ROUND_HALF_CEIL=7,E.ROUND_HALF_FLOOR=8,E.EUCLID=9,E.config=function(){var e,n,t=0,r={},i=arguments,s=i[0],f=s&&"object"==typeof s?function(){return s.hasOwnProperty(n)?null!=(e=s[n]):void 0}:function(){return i.length>t?null!=(e=i[t++]):void 0};return f(n="DECIMAL_PLACES")&&H(e,0,A,2,n)&&(P=0|e),r[n]=P,f(n="ROUNDING_MODE")&&H(e,0,8,2,n)&&(k=0|e),r[n]=k,f(n="EXPONENTIAL_AT")&&(u(e)?H(e[0],-A,0,2,n)&&H(e[1],0,A,2,n)&&(B=0|e[0],$=0|e[1]):H(e,-A,A,2,n)&&(B=-($=0|(0>e?-e:e)))),r[n]=[B,$],f(n="RANGE")&&(u(e)?H(e[0],-A,-1,2,n)&&H(e[1],1,A,2,n)&&(G=0|e[0],z=0|e[1]):H(e,-A,A,2,n)&&(0|e?G=-(z=0|(0>e?-e:e)):j&&L(2,n+" cannot be zero",e))),r[n]=[G,z],f(n="ERRORS")&&(e===!!e||1===e||0===e?(M=0,H=(j=!!e)?x:o):j&&L(2,n+m,e)),r[n]=j,f(n="CRYPTO")&&(e===!!e||1===e||0===e?(V=!(!e||!a),e&&!V&&j&&L(2,"crypto unavailable",a)):j&&L(2,n+m,e)),r[n]=V,f(n="MODULO_MODE")&&H(e,0,9,2,n)&&(W=0|e),r[n]=W,f(n="POW_PRECISION")&&H(e,0,A,2,n)&&(J=0|e),r[n]=J,f(n="FORMAT")&&("object"==typeof e?X=e:j&&L(2,n+" not an object",e)),r[n]=X,r},E.max=function(){return _(arguments,T.lt)},E.min=function(){return _(arguments,T.gt)},E.random=function(){var e=9007199254740992,n=Math.random()*e&2097151?function(){return d(Math.random()*e)}:function(){return 8388608*(1073741824*Math.random()|0)+(8388608*Math.random()|0)};return function(e){var t,r,i,o,u,s=0,f=[],l=new E(q);if(e=null!=e&&H(e,0,A,14)?0|e:P,o=p(e/O),V)if(a&&a.getRandomValues){for(t=a.getRandomValues(new Uint32Array(o*=2));o>s;)u=131072*t[s]+(t[s+1]>>>11),u>=9e15?(r=a.getRandomValues(new Uint32Array(2)),t[s]=r[0],t[s+1]=r[1]):(f.push(u%1e14),s+=2);s=o/2}else if(a&&a.randomBytes){for(t=a.randomBytes(o*=7);o>s;)u=281474976710656*(31&t[s])+1099511627776*t[s+1]+4294967296*t[s+2]+16777216*t[s+3]+(t[s+4]<<16)+(t[s+5]<<8)+t[s+6],u>=9e15?a.randomBytes(7).copy(t,s):(f.push(u%1e14),s+=7);s=o/7}else j&&L(14,"crypto unavailable",a);if(!s)for(;o>s;)u=n(),9e15>u&&(f[s++]=u%1e14);for(o=f[--s],e%=O,o&&e&&(u=S[O-e],f[s]=d(o/u)*u);0===f[s];f.pop(),s--);if(0>s)f=[i=0];else{for(i=-1;0===f[0];f.shift(),i-=O);for(s=1,u=f[0];u>=10;u/=10,s++);O>s&&(i-=O-s)}return l.e=i,l.c=f,l}}(),C=function(){function e(e,n,t){var r,i,o,u,s=0,f=e.length,l=n%R,c=n/R|0;for(e=e.slice();f--;)o=e[f]%R,u=e[f]/R|0,r=c*o+u*l,i=l*o+r%R*R+s,s=(i/t|0)+(r/R|0)+c*u,e[f]=i%t;return s&&e.unshift(s),e}function n(e,n,t,r){var i,o;if(t!=r)o=t>r?1:-1;else for(i=o=0;t>i;i++)if(e[i]!=n[i]){o=e[i]>n[i]?1:-1;break}return o}function r(e,n,t,r){for(var i=0;t--;)e[t]-=i,i=e[t]<n[t]?1:0,e[t]=i*r+e[t]-n[t];for(;!e[0]&&e.length>1;e.shift());}return function(i,o,u,s,f){var l,c,a,h,g,p,m,w,v,N,y,S,R,A,D,F,_,x=i.s==o.s?1:-1,I=i.c,L=o.c;if(!(I&&I[0]&&L&&L[0]))return new E(i.s&&o.s&&(I?!L||I[0]!=L[0]:L)?I&&0==I[0]||!L?0*x:x/0:NaN);for(w=new E(x),v=w.c=[],c=i.e-o.e,x=u+c+1,f||(f=b,c=t(i.e/O)-t(o.e/O),x=x/O|0),a=0;L[a]==(I[a]||0);a++);if(L[a]>(I[a]||0)&&c--,0>x)v.push(1),h=!0;else{for(A=I.length,F=L.length,a=0,x+=2,g=d(f/(L[0]+1)),g>1&&(L=e(L,g,f),I=e(I,g,f),F=L.length,A=I.length),R=F,N=I.slice(0,F),y=N.length;F>y;N[y++]=0);_=L.slice(),_.unshift(0),D=L[0],L[1]>=f/2&&D++;do{if(g=0,l=n(L,N,F,y),0>l){if(S=N[0],F!=y&&(S=S*f+(N[1]||0)),g=d(S/D),g>1)for(g>=f&&(g=f-1),p=e(L,g,f),m=p.length,y=N.length;1==n(p,N,m,y);)g--,r(p,m>F?_:L,m,f),m=p.length,l=1;else 0==g&&(l=g=1),p=L.slice(),m=p.length;if(y>m&&p.unshift(0),r(N,p,y,f),y=N.length,-1==l)for(;n(L,N,F,y)<1;)g++,r(N,y>F?_:L,y,f),y=N.length}else 0===l&&(g++,N=[0]);v[a++]=g,N[0]?N[y++]=I[R]||0:(N=[I[R]],y=1)}while((R++<A||null!=N[0])&&x--);h=null!=N[0],v[0]||v.shift()}if(f==b){for(a=1,x=v[0];x>=10;x/=10,a++);U(w,u+(w.e=a+c*O-1)+1,s,h)}else w.e=c,w.r=+h;return w}}(),h=function(){var e=/^(-?)0([xbo])(?=\w[\w.]*$)/i,n=/^([^.]+)\.$/,t=/^\.([^.]+)$/,r=/^-?(Infinity|NaN)$/,i=/^\s*\+(?=[\w.])|^\s+|\s+$/g;return function(o,u,s,f){var l,c=s?u:u.replace(i,"");if(r.test(c))o.s=isNaN(c)?null:0>c?-1:1;else{if(!s&&(c=c.replace(e,function(e,n,t){return l="x"==(t=t.toLowerCase())?16:"b"==t?2:8,f&&f!=l?e:n}),f&&(l=f,c=c.replace(n,"$1").replace(t,"0.$1")),u!=c))return new E(c,l);j&&L(M,"not a"+(f?" base "+f:"")+" number",u),o.s=null}o.c=o.e=null,M=0}}(),T.absoluteValue=T.abs=function(){var e=new E(this);return e.s<0&&(e.s=1),e},T.ceil=function(){return U(new E(this),this.e+1,2)},T.comparedTo=T.cmp=function(e,n){return M=1,i(this,new E(e,n))},T.decimalPlaces=T.dp=function(){var e,n,r=this.c;if(!r)return null;if(e=((n=r.length-1)-t(this.e/O))*O,n=r[n])for(;n%10==0;n/=10,e--);return 0>e&&(e=0),e},T.dividedBy=T.div=function(e,n){return M=3,C(this,new E(e,n),P,k)},T.dividedToIntegerBy=T.divToInt=function(e,n){return M=4,C(this,new E(e,n),0,1)},T.equals=T.eq=function(e,n){return M=5,0===i(this,new E(e,n))},T.floor=function(){return U(new E(this),this.e+1,3)},T.greaterThan=T.gt=function(e,n){return M=6,i(this,new E(e,n))>0},T.greaterThanOrEqualTo=T.gte=function(e,n){return M=7,1===(n=i(this,new E(e,n)))||0===n},T.isFinite=function(){return!!this.c},T.isInteger=T.isInt=function(){return!!this.c&&t(this.e/O)>this.c.length-2},T.isNaN=function(){return!this.s},T.isNegative=T.isNeg=function(){return this.s<0},T.isZero=function(){return!!this.c&&0==this.c[0]},T.lessThan=T.lt=function(e,n){return M=8,i(this,new E(e,n))<0},T.lessThanOrEqualTo=T.lte=function(e,n){return M=9,-1===(n=i(this,new E(e,n)))||0===n},T.minus=T.sub=function(e,n){var r,i,o,u,s=this,f=s.s;if(M=10,e=new E(e,n),n=e.s,!f||!n)return new E(NaN);if(f!=n)return e.s=-n,s.plus(e);var l=s.e/O,c=e.e/O,a=s.c,h=e.c;if(!l||!c){if(!a||!h)return a?(e.s=-n,e):new E(h?s:NaN);if(!a[0]||!h[0])return h[0]?(e.s=-n,e):new E(a[0]?s:3==k?-0:0)}if(l=t(l),c=t(c),a=a.slice(),f=l-c){for((u=0>f)?(f=-f,o=a):(c=l,o=h),o.reverse(),n=f;n--;o.push(0));o.reverse()}else for(i=(u=(f=a.length)<(n=h.length))?f:n,f=n=0;i>n;n++)if(a[n]!=h[n]){u=a[n]<h[n];break}if(u&&(o=a,a=h,h=o,e.s=-e.s),n=(i=h.length)-(r=a.length),n>0)for(;n--;a[r++]=0);for(n=b-1;i>f;){if(a[--i]<h[i]){for(r=i;r&&!a[--r];a[r]=n);--a[r],a[i]+=b}a[i]-=h[i]}for(;0==a[0];a.shift(),--c);return a[0]?I(e,a,c):(e.s=3==k?-1:1,e.c=[e.e=0],e)},T.modulo=T.mod=function(e,n){var t,r,i=this;return M=11,e=new E(e,n),!i.c||!e.s||e.c&&!e.c[0]?new E(NaN):!e.c||i.c&&!i.c[0]?new E(i):(9==W?(r=e.s,e.s=1,t=C(i,e,0,3),e.s=r,t.s*=r):t=C(i,e,0,W),i.minus(t.times(e)))},T.negated=T.neg=function(){var e=new E(this);return e.s=-e.s||null,e},T.plus=T.add=function(e,n){var r,i=this,o=i.s;if(M=12,e=new E(e,n),n=e.s,!o||!n)return new E(NaN);if(o!=n)return e.s=-n,i.minus(e);var u=i.e/O,s=e.e/O,f=i.c,l=e.c;if(!u||!s){if(!f||!l)return new E(o/0);if(!f[0]||!l[0])return l[0]?e:new E(f[0]?i:0*o)}if(u=t(u),s=t(s),f=f.slice(),o=u-s){for(o>0?(s=u,r=l):(o=-o,r=f),r.reverse();o--;r.push(0));r.reverse()}for(o=f.length,n=l.length,0>o-n&&(r=l,l=f,f=r,n=o),o=0;n;)o=(f[--n]=f[n]+l[n]+o)/b|0,f[n]%=b;return o&&(f.unshift(o),++s),I(e,f,s)},T.precision=T.sd=function(e){var n,t,r=this,i=r.c;if(null!=e&&e!==!!e&&1!==e&&0!==e&&(j&&L(13,"argument"+m,e),e!=!!e&&(e=null)),!i)return null;if(t=i.length-1,n=t*O+1,t=i[t]){for(;t%10==0;t/=10,n--);for(t=i[0];t>=10;t/=10,n++);}return e&&r.e+1>n&&(n=r.e+1),n},T.round=function(e,n){var t=new E(this);return(null==e||H(e,0,A,15))&&U(t,~~e+this.e+1,null!=n&&H(n,0,8,15,w)?0|n:k),t},T.shift=function(e){var n=this;return H(e,-y,y,16,"argument")?n.times("1e"+c(e)):new E(n.c&&n.c[0]&&(-y>e||e>y)?n.s*(0>e?0:1/0):n)},T.squareRoot=T.sqrt=function(){var e,n,i,o,u,s=this,f=s.c,l=s.s,c=s.e,a=P+4,h=new E("0.5");if(1!==l||!f||!f[0])return new E(!l||0>l&&(!f||f[0])?NaN:f?s:1/0);if(l=Math.sqrt(+s),0==l||l==1/0?(n=r(f),(n.length+c)%2==0&&(n+="0"),l=Math.sqrt(n),c=t((c+1)/2)-(0>c||c%2),l==1/0?n="1e"+c:(n=l.toExponential(),n=n.slice(0,n.indexOf("e")+1)+c),i=new E(n)):i=new E(l+""),i.c[0])for(c=i.e,l=c+a,3>l&&(l=0);;)if(u=i,i=h.times(u.plus(C(s,u,a,1))),r(u.c).slice(0,l)===(n=r(i.c)).slice(0,l)){if(i.e<c&&--l,n=n.slice(l-3,l+1),"9999"!=n&&(o||"4999"!=n)){(!+n||!+n.slice(1)&&"5"==n.charAt(0))&&(U(i,i.e+P+2,1),e=!i.times(i).eq(s));break}if(!o&&(U(u,u.e+P+2,0),u.times(u).eq(s))){i=u;break}a+=4,l+=4,o=1}return U(i,i.e+P+1,k,e)},T.times=T.mul=function(e,n){var r,i,o,u,s,f,l,c,a,h,g,p,d,m,w,v=this,N=v.c,y=(M=17,e=new E(e,n)).c;if(!(N&&y&&N[0]&&y[0]))return!v.s||!e.s||N&&!N[0]&&!y||y&&!y[0]&&!N?e.c=e.e=e.s=null:(e.s*=v.s,N&&y?(e.c=[0],e.e=0):e.c=e.e=null),e;for(i=t(v.e/O)+t(e.e/O),e.s*=v.s,l=N.length,h=y.length,h>l&&(d=N,N=y,y=d,o=l,l=h,h=o),o=l+h,d=[];o--;d.push(0));for(m=b,w=R,o=h;--o>=0;){for(r=0,g=y[o]%w,p=y[o]/w|0,s=l,u=o+s;u>o;)c=N[--s]%w,a=N[s]/w|0,f=p*c+a*g,c=g*c+f%w*w+d[u]+r,r=(c/m|0)+(f/w|0)+p*a,d[u--]=c%m;d[u]=r}return r?++i:d.shift(),I(e,d,i)},T.toDigits=function(e,n){var t=new E(this);return e=null!=e&&H(e,1,A,18,"precision")?0|e:null,n=null!=n&&H(n,0,8,18,w)?0|n:k,e?U(t,e,n):t},T.toExponential=function(e,n){return F(this,null!=e&&H(e,0,A,19)?~~e+1:null,n,19)},T.toFixed=function(e,n){return F(this,null!=e&&H(e,0,A,20)?~~e+this.e+1:null,n,20)},T.toFormat=function(e,n){var t=F(this,null!=e&&H(e,0,A,21)?~~e+this.e+1:null,n,21);if(this.c){var r,i=t.split("."),o=+X.groupSize,u=+X.secondaryGroupSize,s=X.groupSeparator,f=i[0],l=i[1],c=this.s<0,a=c?f.slice(1):f,h=a.length;if(u&&(r=o,o=u,u=r,h-=r),o>0&&h>0){for(r=h%o||o,f=a.substr(0,r);h>r;r+=o)f+=s+a.substr(r,o);u>0&&(f+=s+a.slice(r)),c&&(f="-"+f)}t=l?f+X.decimalSeparator+((u=+X.fractionGroupSize)?l.replace(new RegExp("\\d{"+u+"}\\B","g"),"$&"+X.fractionGroupSeparator):l):f}return t},T.toFraction=function(e){var n,t,i,o,u,s,f,l,c,a=j,h=this,g=h.c,p=new E(q),d=t=new E(q),m=f=new E(q);if(null!=e&&(j=!1,s=new E(e),j=a,(!(a=s.isInt())||s.lt(q))&&(j&&L(22,"max denominator "+(a?"out of range":"not an integer"),e),e=!a&&s.c&&U(s,s.e+1,1).gte(q)?s:null)),!g)return h.toString();for(c=r(g),o=p.e=c.length-h.e-1,p.c[0]=S[(u=o%O)<0?O+u:u],e=!e||s.cmp(p)>0?o>0?p:d:s,u=z,z=1/0,s=new E(c),f.c[0]=0;l=C(s,p,0,1),i=t.plus(l.times(m)),1!=i.cmp(e);)t=m,m=i,d=f.plus(l.times(i=d)),f=i,p=s.minus(l.times(i=p)),s=i;return i=C(e.minus(t),m,0,1),f=f.plus(i.times(d)),t=t.plus(i.times(m)),f.s=d.s=h.s,o*=2,n=C(d,m,o,k).minus(h).abs().cmp(C(f,t,o,k).minus(h).abs())<1?[d.toString(),m.toString()]:[f.toString(),t.toString()],z=u,n},T.toNumber=function(){return+this},T.toPower=T.pow=function(e,n){var t,r,i,o=d(0>e?-e:+e),u=this;if(null!=n&&(M=23,n=new E(n)),!H(e,-y,y,23,"exponent")&&(!isFinite(e)||o>y&&(e/=0)||parseFloat(e)!=e&&!(e=NaN))||0==e)return t=Math.pow(+u,e),new E(n?t%n:t);for(n?e>1&&u.gt(q)&&u.isInt()&&n.gt(q)&&n.isInt()?u=u.mod(n):(i=n,n=null):J&&(t=p(J/O+2)),r=new E(q);;){if(o%2){if(r=r.times(u),!r.c)break;t?r.c.length>t&&(r.c.length=t):n&&(r=r.mod(n))}if(o=d(o/2),!o)break;u=u.times(u),t?u.c&&u.c.length>t&&(u.c.length=t):n&&(u=u.mod(n))}return n?r:(0>e&&(r=q.div(r)),i?r.mod(i):t?U(r,J,k):r)},T.toPrecision=function(e,n){return F(this,null!=e&&H(e,1,A,24,"precision")?0|e:null,n,24)},T.toString=function(e){var n,t=this,i=t.s,o=t.e;return null===o?i?(n="Infinity",0>i&&(n="-"+n)):n="NaN":(n=r(t.c),n=null!=e&&H(e,2,64,25,"base")?D(l(n,o),0|e,10,i):B>=o||o>=$?f(n,o):l(n,o),0>i&&t.c[0]&&(n="-"+n)),n},T.truncated=T.trunc=function(){return U(new E(this),this.e+1,1)},T.valueOf=T.toJSON=function(){var e,n=this,t=n.e;return null===t?n.toString():(e=r(n.c),e=B>=t||t>=$?f(e,t):l(e,t),n.s<0?"-"+e:e)},null!=e&&E.config(e),E}function t(e){var n=0|e;return e>0||e===n?n:n-1}function r(e){for(var n,t,r=1,i=e.length,o=e[0]+"";i>r;){for(n=e[r++]+"",t=O-n.length;t--;n="0"+n);o+=n}for(i=o.length;48===o.charCodeAt(--i););return o.slice(0,i+1||1)}function i(e,n){var t,r,i=e.c,o=n.c,u=e.s,s=n.s,f=e.e,l=n.e;if(!u||!s)return null;if(t=i&&!i[0],r=o&&!o[0],t||r)return t?r?0:-s:u;if(u!=s)return u;if(t=0>u,r=f==l,!i||!o)return r?0:!i^t?1:-1;if(!r)return f>l^t?1:-1;for(s=(f=i.length)<(l=o.length)?f:l,u=0;s>u;u++)if(i[u]!=o[u])return i[u]>o[u]^t?1:-1;return f==l?0:f>l^t?1:-1}function o(e,n,t){return(e=c(e))>=n&&t>=e}function u(e){return"[object Array]"==Object.prototype.toString.call(e)}function s(e,n,t){for(var r,i,o=[0],u=0,s=e.length;s>u;){for(i=o.length;i--;o[i]*=n);for(o[r=0]+=N.indexOf(e.charAt(u++));r<o.length;r++)o[r]>t-1&&(null==o[r+1]&&(o[r+1]=0),o[r+1]+=o[r]/t|0,o[r]%=t)}return o.reverse()}function f(e,n){return(e.length>1?e.charAt(0)+"."+e.slice(1):e)+(0>n?"e":"e+")+n}function l(e,n){var t,r;if(0>n){for(r="0.";++n;r+="0");e=r+e}else if(t=e.length,++n>t){for(r="0",n-=t;--n;r+="0");e+=r}else t>n&&(e=e.slice(0,n)+"."+e.slice(n));return e}function c(e){return e=parseFloat(e),0>e?p(e):d(e)}var a,h,g=/^-?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?$/i,p=Math.ceil,d=Math.floor,m=" not a boolean or binary digit",w="rounding mode",v="number type has more than 15 significant digits",N="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$_",b=1e14,O=14,y=9007199254740991,S=[1,10,100,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12,1e13],R=1e7,A=1e9;if("undefined"!=typeof crypto&&(a=crypto),"function"==typeof define&&define.amd)define(function(){return n()});else if("undefined"!=typeof module&&module.exports){if(module.exports=n(),!a)try{a=require("crypto")}catch(E){}}else e||(e="undefined"!=typeof self?self:Function("return this")()),e.BigNumber=n()}(this);
  </script>
  
  <style>
    body{
      font-family: 'HelveticaNeue-Light', 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', 'Lucida Grande', sans-serif;
      background: #E2E2E2;
    }
    *, *:after, *:before {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    #pleasewait{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
    }
    #infomessage {
      text-align: center;
      font-size: 1rem;
      margin: 0 2rem 4.5rem;
    }
    
    .wrapper{
      background: #E2E2E2;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      display:none;
      text-align: center;
    }
    .title {
      text-align: center;
      font-size: 1.2rem;
      margin: 1rem 0rem;
    }
    .message {
      text-align: center;
      font-size: 1rem;
      /*margin: 0 2rem 4.5rem;*/
    }
    
    #passwordField {
      text-align: center;
      font-size: 1rem;
      margin: 1rem 0rem;
      /*margin: 0 2rem 4.5rem;*/
    }
    
    .wrapper button {
      background: transparent;
      border: none;
      color: #1678E5;
      height: 3rem;
      font-size: 1rem;
      width: 50%;
      position: absolute;
      bottom: 0;
      cursor: pointer;
    }
    #cancel-button {
      border-top: 1px solid #B4B4B4;
      border-right: 1px solid #B4B4B4;
      left: 0;
      border-radius: 0 0 0 10px;
    }
    #confirm-button {
      border-top: 1px solid #B4B4B4;
      right: 0;
      border-radius: 0 0 10px 0;
    }
    .wrapper button:focus,
    .wrapper button:hover {
      font-weight: bold;
      background: #EFEFEF;
    }
    .wrapper button:active {
      background: #D6D6D6;
    }
    
    .button {
      margin: 1rem 0rem;
      display: inline-block;
      padding: 9px 15px;
      background-color: #3898EC;
      color: white;
      border: 0;
      line-height: inherit;
      text-decoration: none;
      cursor: pointer;
      border-radius: 0;
    }

    input.button {
      -webkit-appearance: button;
    }
  </style>
  
  <body>

    <div id="pleasewait">
      <br/>
      <p id="infomessage">Please wait...</p>
    </div>
    
    <form id="form" class="wrapper">
      <br/>
      <p id="message" class="message"></p>
      <p id="passwordField"><label>Password Required:</label><input id="password" type="password" /></p>
      <button id="cancel-button" type="button" autofocus>Cancel</button>
      <button id="confirm-button" type="button" >Confirm</button>
    </form>
  
    <div id="modal-dialog" class="wrapper">
      <h3 id="modal-dialog-title" class="title">Title</h3>
      <p id="modal-dialog-message" class="message">Message</p>
      <span id="modal-dialog-button" class="button">Ok</span>
    </div>
      
    <script>
    var noMessageReceivedYet = true;
    var closedByCode = false;
    var pleaseWait = document.getElementById("pleasewait");
    var form = document.getElementById("form");
    var cancelButton = document.getElementById("cancel-button");
    var confirmButton = document.getElementById("confirm-button");
    var message = document.getElementById("message");
    var infoMessage = document.getElementById("infomessage");
    var password = document.getElementById("password");
    var passwordField = document.getElementById("passwordField");
    var modalDialog = document.getElementById("modal-dialog");
    var modalDialogButton = document.getElementById("modal-dialog-button");
    var modalDialogTitle = document.getElementById("modal-dialog-title");
    var modalDialogMessage = document.getElementById("modal-dialog-message");
    
    var firstUrl = null;
    
    var inIframe = true;
    var source = null;
    if(window.opener){
      inIframe = false;
      source = window.opener;
    }else if(window.parent != window){
      source = window.parent;
    }else{
      console.log("closing");
      window.close();
    }
    
    function closeWindow(){
      closedByCode = true;
      window.close();
    }
    
    function showWaiting(text){
      if(!text){
        text = "Please wait..."
      }
      infoMessage.innerHTML = text;
      pleaseWait.style.display = "block";
      form.style.display = "none";
    }
    
    function hideWaiting(){
      pleaseWait.style.display = "none";
      form.style.display = "block";
      
      window.onbeforeunload = null;
    }
      
    function showMessage(title, message, callback, buttonText){
      modalDialog.style.display = "block";
      modalDialogTitle.innerHTML = title;
      modalDialogMessage.innerHTML = "";
      if((typeof message) == "string"){
        modalDialogMessage.innerHTML += message;
      }else{
        modalDialogMessage.appendChild(message);
      }
      modalDialogMessage.appendChild(document.createElement('br'));
      
      if(!buttonText){
        buttonText = "Ok";
      }
      modalDialogButton.innerHTML = buttonText;
      modalDialogButton.onclick = function(){
        modalDialogButton.onclick = null;
        modalDialog.style.display = "none";
        if(callback){
          callback();
        }
      }
    }
    
    function hideMessage(){
      modalDialog.style.display = "none";
      modalDialogButton.onclick = null;
    }
      
    function sendAsync(url,payload, callback) {
      var request = new XMLHttpRequest();
      request.open('POST', url, true);
      request.setRequestHeader('Content-Type','application/json'); 

      request.onreadystatechange = function() {
        if (request.readyState === 4) {
          var result = request.responseText;
          var error = null;
          try {
            result = JSON.parse(result);
          } catch(e) {
            var message = !!result && !!result.error && !!result.error.message ? result.error.message : 'Invalid JSON RPC response: ' + JSON.stringify(result);
            error = {message:message,type:"JsonParse"};
          }
          callback(error, result);
        }
      };
      
      try {
        request.send(JSON.stringify(payload));
      } catch(e) {
        callback({message:'CONNECTION ERROR: Couldn\'t connect to node '+ url +'.',type:"noConnection"});
      }
    }
    
    function addBlocky(message, address){
      var icon = blockies.create({ 
        seed: address,
        size: 8,
        scale: 6
      });
      message.appendChild(icon);
    }
    
    function askAuthorization(transactionInfo, data, requireUnlock, sourceWindow){
      
        
      var value = transactionInfo["value"] ? transactionInfo.value : "0";
      var gasProvided = transactionInfo.gas;
      var gasPriceProvided = transactionInfo.gasPrice;
      var gasPrice = new BigNumber(gasPriceProvided,16); 
      var gas = new BigNumber(gasProvided,16);
      var weiValue = new BigNumber(value,16);
      var gasWeiValue = gas.times(gasPrice);
      var etherValue = weiValue.dividedBy(new BigNumber("1000000000000000000"));
      var gasEtherValue = gasWeiValue.dividedBy(new BigNumber("1000000000000000000"));
      
      hideWaiting();
      
      message.innerHTML = "";
      
      addBlocky(message,transactionInfo.from);
      
      var span = document.createElement('span');
      span.style="font-size:3em;";
      span.innerHTML = "&nbsp;&nbsp;&nbsp;" + "&#x2192;" + "&nbsp;&nbsp;&nbsp;";
      message.appendChild(span);
      
      addBlocky(message,transactionInfo.to);
      
      message.appendChild(document.createElement('br'));
      var textSpan = document.createElement("span");
      message.appendChild(textSpan);
      textSpan.innerHTML = etherValue.toFormat() + " ether <br/>  + gas cost (" + gasEtherValue.toFormat() + " ether )"
      
      if(requireUnlock){
        passwordField.style.display = "block"; 
      }else{
        passwordField.style.display = "none"; 
      }
      
      cancelButton.onclick = function(){
        sourceWindow.postMessage({id:data.id,result:null,error:{message:"Not Authorized"},type:"cancel"},firstUrl);
        closeWindow();
      }
      
      var submitFunc = function(){
        window.onbeforeunload = function (event) {
          if(!closedByCode){
            return "do not close now as a transaction is progress, this cannot be canceled and we wait for an answer";
          }
        };
        if(requireUnlock){
          if(password.value == ""){
            password.style.border = "2px solid red";
            return false;
          }
          password.style.border = "none";
          var params = [transactionInfo.from,password.value,3];
          showWaiting("Please wait...<br/>Do not close the window.");
          sendAsync(data.url,{id:999992,method:"personal_unlockAccount",params:params},function(error,result){
            if(error || result.error){
              showMessage("Error unlocking account", "Please retry.", hideWaiting);
            }else{
              sendAsync(data.url,data.payload,function(error,result){
                sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
                closeWindow();
              });
            }
          });
        }else{
          sendAsync(data.url,data.payload,function(error,result){
            if(result && result.error){
              processMessage(data,sourceWindow);
            }else{
              sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
              closeWindow();
            }
          });
          showWaiting();
        }
        return false;
      }
      
      form.onsubmit = submitFunc;
      confirmButton.onclick = submitFunc;
    }
    
    function needToAndCanUnlockAccount(address,url,callback){
      sendAsync(url,{id:9999990,method:"eth_sign",params:[address,"0xc6888fa8d57087278718986382264244252f8d57087278718986382264244252f"]},function(error,result){
        if(error || result.error){
          sendAsync(url,{id:9999991,method:"personal_listAccounts",params:[]},function(error,result){
            if(error || result.error){
              callback(true,false);
            }else{
              callback(true,true);
            }
          });
        }else{
          callback(false);
        }
      });
    }
      
    function receiveMessage(event){
      if(event.source != source){
        return;
      }
      if(firstUrl){
        if(firstUrl != event.origin){
          return;
        }
      }else{
        firstUrl = event.origin;
      }
      hideMessage();
      noMessageReceivedYet = false;
      var data = event.data;
      try{
        processMessage(data,event.source);
      }catch(e){
        event.source.postMessage({id:data.id,result:null,error:{message:"Could not process message data"},type:"notValid"},firstUrl);
        showMessage("Error","The application has sent invalid data", function(){
          closeWindow();
        });
      }
      
    }
    
    var allowedMethods = [
       "web3_clientVersion"
      ,"web3_sha3"
      ,"net_version"
      ,"net_peerCount"
      ,"net_listening"
      ,"eth_protocolVersion"
      ,"eth_syncing"
      ,"eth_coinbase"
      ,"eth_mining"
      ,"eth_hashrate"
      ,"eth_gasPrice"
      ,"eth_accounts"
      ,"eth_blockNumber"
      ,"eth_getBalance"
      ,"eth_getStorageAt"
      ,"eth_getTransactionCount"
      ,"eth_getBlockTransactionCountByHash"
      ,"eth_getBlockTransactionCountByNumber"
      ,"eth_getUncleCountByBlockHash"
      ,"eth_getUncleCountByBlockNumber"
      ,"eth_getCode"
      ,"eth_sendRawTransaction"
      ,"eth_call"
      ,"eth_estimateGas"
      ,"eth_getBlockByHash"
      ,"eth_getBlockByNumber"
      ,"eth_getTransactionByHash"
      ,"eth_getTransactionByBlockHashAndIndex"
      ,"eth_getTransactionByBlockNumberAndIndex"
      ,"eth_getTransactionReceipt"
      ,"eth_getUncleByBlockHashAndIndex"
      ,"eth_getUncleByBlockNumberAndIndex"
      ,"eth_getCompilers"
      ,"eth_compileLLL"
      ,"eth_compileSolidity"
      ,"eth_compileSerpent"
      ,"eth_newFilter"
      ,"eth_newBlockFilter"
      ,"eth_newPendingTransactionFilter"
      ,"eth_uninstallFilter"
      ,"eth_getFilterChanges"
      ,"eth_getFilterLogs"
      ,"eth_getLogs"
      ,"eth_getWork"
      ,"eth_submitWork"
      ,"eth_submitHashrate"
      // ,"shh_post"
      // ,"shh_version"
      // ,"shh_newIdentity"
      // ,"shh_hasIdentity"
      // ,"shh_newGroup"
      // ,"shh_addToGroup"
      // ,"shh_newFilter"
      // ,"shh_uninstallFilter"
      // ,"shh_getFilterChanges"
      // ,"shh_getMessages"
    ];
    
    function isMethodAllowed(method){
      return allowedMethods.indexOf(method) != -1;
    }
    
    function processMessage(data, sourceWindow){
      
      if(inIframe){
        if(isMethodAllowed(data.payload.method)){
          sendAsync(data.url,data.payload,function(error,result){
            sourceWindow.postMessage({id:data.id,result:result,error:error},firstUrl);
          });
        }else{
          sourceWindow.postMessage({id:data.id,result:null,error:{message:"method (" + data.payload.method + ") not allowed in iframe"},type:"notAllowed"},firstUrl);
        }
      }else if(data.payload.method == "eth_sendTransaction"){
        var transactionInfo = null;
        if(data.payload.params.length > 0){ 
          if(data.payload.params[0]["gas"] && data.payload.params[0]["gasPrice"] && data.payload.params[0]["to"] && data.payload.params[0]["from"]){
            transactionInfo = data.payload.params[0];
          }
        }
        if(transactionInfo != null){
          needToAndCanUnlockAccount(transactionInfo.from,data.url,function(requireUnlock,canUnlock){
            if(requireUnlock && canUnlock){
              askAuthorization(transactionInfo,data,true, sourceWindow);
            }else if(!requireUnlock){
              askAuthorization(transactionInfo,data,false,sourceWindow);
            }else if(requireUnlock && !canUnlock){
              var messageHtml = document.createElement('span');
              addBlocky(messageHtml,transactionInfo.from); 
              messageHtml.appendChild(document.createElement('br'));
              var span = document.createElement('span');
              span.innerHTML = "You need to unlock your account first : <br/>" + transactionInfo.from;
              messageHtml.appendChild(span);
              
              showMessage("Account Locked",messageHtml,function(){
                processMessage(data,sourceWindow);
              }, "Done");
            }
            
          });
        }else{
          sourceWindow.postMessage({id:data.id,result:null,error:{message:"Need to specify from , to, gas and gasPrice"},type:"notValid"},firstUrl);
          closeWindow();
        }
      }else{
        sourceWindow.postMessage({id:data.id,result:null,error:{message:"method (" + data.payload.method + ") not allowed in popup"},type:"notAllowed"},firstUrl);
      }     
    }
    
    function checkMessageNotReceived(){
      if(noMessageReceivedYet){
        showMessage("Error","No transaction received. Please make sure popup are not blocked.", function(){
          closeWindow();
        });
      }
    }
    setTimeout(checkMessageNotReceived,1000);
    
    window.addEventListener("message", receiveMessage);
    if(source){
      source.postMessage("ready","*");
    }
    
    </script>
  </body>
</html>
```


#eip-137.md
<pre>
  EIP: 137
  Title: Ethereum Domain Name Service - Specification
  Author: Nick Johnson <arachnid@notdot.net>
  Status: Final
  Type: Standards Track
  Category: ERC
  Created: 2016-04-04
</pre>

# Abstract

This draft EIP describes the details of the Ethereum Name Service, a proposed protocol and ABI definition that provides flexible resolution of short, human-readable names to service and resource identifiers. This permits users and developers to refer to human-readable and easy to remember names, and permits those names to be updated as necessary when the underlying resource (contract, content-addressed data, etc) changes. 

The goal of domain names is to provide stable, human-readable identifiers that can be used to specify network resources. In this way, users can enter a memorable string, such as 'vitalik.wallet' or 'www.mysite.swarm', and be directed to the appropriate resource. The mapping between names and resources may change over time, so a user may change wallets, a website may change hosts, or a swarm document may be updated to a new version, without the domain name changing. Further, a domain need not specify a single resource; different record types allow the same domain to reference different resources. For instance, a browser may resolve 'mysite.swarm' to the IP address of its server by fetching its A (address) record, while a mail client may resolve the same address to a mail server by fetching its MX (mail exchanger) record.
# Motivation

Existing [specifications](https://github.com/ethereum/wiki/wiki/Registrar-ABI) and [implementations](https://ethereum.gitbooks.io/frontier-guide/content/registrar_services.html) for name resolution in Ethereum provide basic functionality, but suffer several shortcomings that will significantly limit their long-term usefulness:
- A single global namespace for all names with a single 'centralised' resolver.
- Limited or no support for delegation and sub-names/sub-domains.
- Only one record type, and no support for associating multiple copies of a record with a domain.
- Due to a single global implementation, no support for multiple different name allocation systems.
- Conflation of responsibilities: Name resolution, registration, and whois information.

Use-cases that these features would permit include:
- Support for subnames/sub-domains - eg, live.mysite.tld and forum.mysite.tld.
- Multiple services under a single name, such as a DApp hosted in Swarm, a Whisper address, and a mail server.
- Support for DNS record types, allowing blockchain hosting of 'legacy' names. This would permit an Ethereum client such as Mist to resolve the address of a traditional website, or the mail server for an email address, from a blockchain name.
- DNS gateways, exposing ENS domains via the Domain Name Service, providing easier means for legacy clients to resolve and connect to blockchain services.

The first two use-cases, in particular, can be observed everywhere on the present-day internet under DNS, and we believe them to be fundamental features of a name service that will continue to be useful as the Ethereum platform develops and matures.

The normative parts of this document does not specify an implementation of the proposed system; its purpose is to document a protocol that different resolver implementations can adhere to in order to facilitate consistent name resolution. An appendix provides sample implementations of resolver contracts and libraries, which should be treated as illustrative examples only.

Likewise, this document does not attempt to specify how domains should be registered or updated, or how systems can find the owner responsible for a given domain. Registration is the responsibility of registrars, and is a governance matter that will necessarily vary between top-level domains.

Updating of domain records can also be handled separately from resolution. Some systems, such as swarm, may require a well defined interface for updating domains, in which event we anticipate the development of a standard for this.
# Specification
## Overview

The ENS system comprises three main parts:
- The ENS registry
- Resolvers
- Registrars

The registry is a single contract that provides a mapping from any registered name to the resolver responsible for it, and permits the owner of a name to set the resolver address, and to create subdomains, potentially with different owners to the parent domain.

Resolvers are responsible for performing resource lookups for a name - for instance, returning a contract address, a content hash, or IP address(es) as appropriate. The resolver specification, defined here and extended in other EIPs, defines what methods a resolver may implement to support resolving different types of records.

Registrars are responsible for allocating domain names to users of the system, and are the only entities capable of updating the ENS; the owner of a node in the ENS registry is its registrar. Registrars may be contracts or externally owned accounts, though it is expected that the root and top-level registrars, at a minimum, will be implemented as contracts.

Resolving a name in ENS is a two-step process. First, the ENS registry is called with the name to resolve, after hashing it using the procedure described below. If the record exists, the registry returns the address of its resolver. Then, the resolver is called, using the method appropriate to the resource being requested. The resolver then returns the desired result.

For example, suppose you wish to find the address of the token contract associated with 'beercoin.eth'. First, get the resolver:

```
var node = namehash("beercoin.eth");
var resolver = ens.resolver(node);
```

Then, ask the resolver for the address for the contract:

```
var hash = resolver.addr(node);
```

Because the `namehash` procedure depends only on the name itself, this can be precomputed and inserted into a contract, removing the need for string manipulation, and permitting O(1) lookup of ENS records regardless of the number of components in the raw name.
## Name Syntax

ENS names must conform to the following syntax:

<pre>&lt;domain> ::= &lt;label> | &lt;domain> "." &lt;label>
&lt;label> ::= any valid string label per [UTS46](http://unicode.org/reports/tr46/)
</pre>

In short, names consist of a series of dot-separated labels. Each label must be a valid normalised label as described in [UTS46](http://unicode.org/reports/tr46/) with the options `transitional=false` and `useSTD3AsciiRules=true`. For Javascript implementations, a [library](https://www.npmjs.com/package/idna-uts46) is available that normalises and checks names.

Note that while upper and lower case letters are allowed in names, the UTS46 normalisation process case-folds labels before hashing them, so two names with different case but identical spelling will produce the same namehash.

Labels and domains may be of any length, but for compatibility with legacy DNS, it is recommended that labels be restricted to no more than 64 characters each, and complete ENS names to no more than 255 characters. For the same reason, it is recommended that labels do not start or end with hyphens, or start with digits.

## namehash algorithm

Before being used in ENS, names are hashed using the 'namehash' algorithm. This algorithm recursively hashes components of the name, producing a unique, fixed-length string for any valid input domain. The output of namehash is referred to as a 'node'.

Pseudocode for the namehash algorithm is as follows:

```
def namehash(name):
  if name == '':
    return '\0' * 32
  else:
    label, _, remainder = name.partition('.')
    return sha3(namehash(remainder) + sha3(label))
```

Informally, the name is split into labels, each label is hashed. Then, starting with the last component, the previous output is concatenated with the label hash and hashed again. The first component is concatenated with 32 '0' bytes. Thus, 'mysite.swarm' is processed as follows:

```
node = '\0' * 32
node = sha3(node + sha3('swarm'))
node = sha3(node + sha3('mysite'))
```

Implementations should conform to the following test vectors for namehash:

    namehash('') = 0x0000000000000000000000000000000000000000000000000000000000000000
    namehash('eth') = 0x93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae
    namehash('foo.eth') = 0xde9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f

## Registry specification

The ENS registry contract exposes the following functions:

```
function owner(bytes32 node) constant returns (address);
```

Returns the owner (registrar) of the specified node.

```
function resolver(bytes32 node) constant returns (address);
```

Returns the resolver for the specified node.

```
function ttl(bytes32 node) constant returns (uint64);
```

Returns the time-to-live (TTL) of the node; that is, the maximum duration for which a node's information may be cached.

```
function setOwner(bytes32 node, address owner);
```

Transfers ownership of a node to another registrar. This function may only be called by the current owner of `node`. A successful call to this function logs the event `Transfer(bytes32 indexed, address)`.

```
function setSubnodeOwner(bytes32 node, bytes32 label, address owner);
```

Creates a new node, `sha3(node, label)` and sets its owner to `owner`, or updates the node with a new owner if it already exists. This function may only be called by the current owner of `node`. A successful call to this function logs the event `NewOwner(bytes32 indexed, bytes32 indexed, address)`.

```
function setResolver(bytes32 node, address resolver);
```

Sets the resolver address for `node`. This function may only be called by the owner of `node`. A successful call to this function logs the event `NewResolver(bytes32 indexed, address)`.

```
function setTTL(bytes32 node, uint64 ttl);
```

Sets the TTL for a node. A node's TTL applies to the 'owner' and 'resolver' records in the registry, as well as to any information returned by the associated resolver.
## Resolver specification

Resolvers may implement any subset of the record types specified here. Where a record types specification requires a resolver to provide multiple functions, the resolver MUST implement either all or none of them. Resolvers MUST specify a fallback function that throws.

Resolvers have one mandatory function:

```
function supportsInterface(bytes4 interfaceID) constant returns (bool)
```

The `supportsInterface` function is documented in [EIP 165](https://github.com/ethereum/EIPs/issues/165), and returns true if the resolver implements the interface specified by the provided 4 byte identifier. An interface identifier consists of the XOR of the function signature hashes of the functions provided by that interface; in the degenerate case of single-function interfaces, it is simply equal to the signature hash of that function. If a resolver returns `true` for `supportsInterface()`, it must implement the functions specified in that interface.

`supportsInterface` must always return true for `0x01ffc9a7`, which is the interface ID of `supportsInterface` itself.

 Currently standardised resolver interfaces are specified in the table below.

The following interfaces are defined:

| Interface name | Interface hash | Specification |
| --- | --- | --- |
| `addr` | 0x3b3b57de | [Contract address](#addr) |
| `name`      | 0x691f3431   | #181    |
| `ABI`       | 0x2203ab56   | #205    |
| `pubkey`    | 0xc8690233   | #619    |

EIPs may define new interfaces to be added to this registry.

### <a name="addr"></a>Contract Address Interface

Resolvers wishing to support contract address resources must provide the following function:

```
function addr(bytes32 node) constant returns (address);
```

If the resolver supports `addr` lookups but the requested node does not have a record, the resolver MUST return the zero address.

Clients resolving the `addr` record MUST check for a zero return value, and treat this in the same manner as a name that does not have a resolver specified - that is, refuse to send funds to or interact with the address. Failure to do this can result in users accidentally sending funds to the 0 address.

Changes to an address MUST trigger the following event:

```
event AddrChanged(bytes32 indexed node, address a);
```
# Appendix A: Registry Implementation

```
contract ENS {
    struct Record {
        address owner;
        address resolver;
        uint64 ttl;
    }

    mapping(bytes32=>Record) records;

    event NewOwner(bytes32 indexed node, bytes32 indexed label, address owner);
    event Transfer(bytes32 indexed node, address owner);
    event NewResolver(bytes32 indexed node, address resolver);

    modifier only_owner(bytes32 node) {
        if(records[node].owner != msg.sender) throw;
        _
    }

    function ENS(address owner) {
        records[0].owner = owner;
    }

    function owner(bytes32 node) constant returns (address) {
        return records[node].owner;
    }

    function resolver(bytes32 node) constant returns (address) {
        return records[node].resolver;
    }

    function ttl(bytes32 node) constant returns (uint64) {
        return records[node].ttl;
    }

    function setOwner(bytes32 node, address owner) only_owner(node) {
        Transfer(node, owner);
        records[node].owner = owner;
    }

    function setSubnodeOwner(bytes32 node, bytes32 label, address owner) only_owner(node) {
        var subnode = sha3(node, label);
        NewOwner(node, label, owner);
        records[subnode].owner = owner;
    }

    function setResolver(bytes32 node, address resolver) only_owner(node) {
        NewResolver(node, resolver);
        records[node].resolver = resolver;
    }

    function setTTL(bytes32 node, uint64 ttl) only_owner(node) {
        NewTTL(node, ttl);
        records[node].ttl = ttl;
    }
}
```
# Appendix B: Sample Resolver Implementations
### Built-in resolver

The simplest possible resolver is a contract that acts as its own name resolver by implementing the contract address resource profile:

```
contract DoSomethingUseful {
    // Other code

    function addr(bytes32 node) constant returns (address) {
        return this;
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```

Such a contract can be inserted directly into the ENS registry, eliminating the need for a separate resolver contract in simple use-cases. However, the requirement to 'throw' on unknown function calls may interfere with normal operation of some types of contract.

### Standalone resolver

A basic resolver that implements the contract address profile, and allows only its owner to update records:

```
contract Resolver {
    event AddrChanged(bytes32 indexed node, address a);

    address owner;
    mapping(bytes32=>address) addresses;

    modifier only_owner() {
        if(msg.sender != owner) throw;
        _
    }

    function Resolver() {
        owner = msg.sender;
    }

    function addr(bytes32 node) constant returns(address) {
        return addresses[node];    
    }

    function setAddr(bytes32 node, address addr) only_owner {
        addresses[node] = addr;
        AddrChanged(node, addr);
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```

After deploying this contract, use it by updating the ENS registry to reference this contract for a name, then calling `setAddr()` with the same node to set the contract address it will resolve to.
### Public resolver

Similar to the resolver above, this contract only supports the contract address profile, but uses the ENS registry to determine who should be allowed to update entries:

```
contract PublicResolver {
    event AddrChanged(bytes32 indexed node, address a);
    event ContentChanged(bytes32 indexed node, bytes32 hash);

    ENS ens;
    mapping(bytes32=>address) addresses;

    modifier only_owner(bytes32 node) {
        if(ens.owner(node) != msg.sender) throw;
        _
    }

    function PublicResolver(address ensAddr) {
        ens = ENS(ensAddr);
    }

    function addr(bytes32 node) constant returns (address ret) {
        ret = addresses[node];
    }

    function setAddr(bytes32 node, address addr) only_owner(node) {
        addresses[node] = addr;
        AddrChanged(node, addr);
    }

    function supportsInterface(bytes4 interfaceID) constant returns (bool) {
        return interfaceID == 0x3b3b57de || interfaceID == 0x01ffc9a7;
    }

    function() {
        throw;
    }
}
```
# Appendix C: Sample Registrar Implementation

This registrar allows users to register names at no cost if they are the first to request them.

```
contract FIFSRegistrar {
    ENS ens;
    bytes32 rootNode;

    function FIFSRegistrar(address ensAddr, bytes32 node) {
        ens = ENS(ensAddr);
        rootNode = node;
    }

    function register(bytes32 subnode, address owner) {
        var node = sha3(rootNode, subnode);
        var currentOwner = ens.owner(node);
        if(currentOwner != 0 && currentOwner != msg.sender)
            throw;

        ens.setSubnodeOwner(rootNode, subnode, owner);
    }
}
```


#eip-141.md
## Preamble

    EIP: 141
    Title: Designated invalid EVM instruction
    Author: Alex Beregszaszi
    Type: Standard Track
    Category: Core
    Status: Accepted
    Created: 2017-02-09

## Abstract

An instruction is designated to remain as an invalid instruction.

## Motivation

The invalid instruction can be used as a distinct reason to abort execution.

## Specification

The opcode `0xfe` is the `INVALID` instruction. It can be used to abort the execution (i.e. duplicates as an `ABORT` instruction).

## Backwards Compatibility

This instruction was never used and therefore has no effect on past contracts.

## Copyright

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).


#eip-150.md
## Preamble
```
EIP: 150
Title: Gas cost changes for IO-heavy operations
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-09-24
```

### Specification

If `block.number >= FORK_BLKNUM`, then:
- Increase the gas cost of EXTCODESIZE to 700
- Increase the base gas cost of EXTCODECOPY to 700
- Increase the gas cost of BALANCE to 400
- Increase the gas cost of SLOAD to 200
- Increase the gas cost of CALL, DELEGATECALL, CALLCODE to 700
- Increase the gas cost of SELFDESTRUCT to 5000
- If SELFDESTRUCT hits a newly created account, it triggers an additional gas cost of 25000 (similar to CALLs)
- Increase the recommended gas limit target to 5.5 million
- Define "all but one 64th" of `N` as `N - floor(N / 64)`
- If a call asks for more gas than the maximum allowed amount (ie. total amount of gas remaining in the parent after subtracting the gas cost of the call and memory expansion), do not return an OOG error; instead, if a call asks for more gas than all but one 64th of the maximum allowed amount, call with all but one 64th of the maximum allowed amount of gas (this is equivalent to a version of #90 plus #114). CREATE only provides all but one 64th of the parent gas to the child call.

That is, substitute:

```
        extra_gas = (not ext.account_exists(to)) * opcodes.GCALLNEWACCOUNT + \
            (value > 0) * opcodes.GCALLVALUETRANSFER
        if compustate.gas < gas + extra_gas:
            return vm_exception('OUT OF GAS', needed=gas+extra_gas)
        submsg_gas = gas + opcodes.GSTIPEND * (value > 0)
```

With:

```
        def max_call_gas(gas):
          return gas - (gas // 64)

        extra_gas = (not ext.account_exists(to)) * opcodes.GCALLNEWACCOUNT + \
            (value > 0) * opcodes.GCALLVALUETRANSFER
        if compustate.gas < extra_gas:
            return vm_exception('OUT OF GAS', needed=extra_gas)
        if compustate.gas < gas + extra_gas:
            gas = min(gas, max_call_gas(compustate.gas - extra_gas))
        submsg_gas = gas + opcodes.GSTIPEND * (value > 0)
```

### Rationale

Recent denial-of-service attacks have shown that opcodes that read the state tree are under-priced relative to other opcodes. There are software changes that have been made, are being made and can be made in order to mitigate the situation; however, the fact will remain that such opcodes will be by a substantial margin the easiest known mechanism to degrade network performance via transaction spam. The concern arises because it takes a long time to read from disk, and is additionally a risk to future sharding proposals as the "attack transactions" that have so far been most successful in degrading network performance would also require tens of megabytes to provide Merkle proofs for. This EIP increases the cost of storage reading opcodes to address this concern. The costs have been derived from an updated version of the calculation table used to generate the 1.0 gas costs: https://docs.google.com/spreadsheets/d/15wghZr-Z6sRSMdmRmhls9dVXTOpxKy8Y64oy9MvDZEQ/edit#gid=0 ; the rules attempt to target a limit of 8 MB of data that needs to be read in order to process a block, and include an estimate of 500 bytes for a Merkle proof for SLOAD and 1000 for an account.

This EIP aims to be simple, and adds a flat penalty of 300 gas on top of the costs calculated in this table to account for the cost of loading the code (~17-21 kb in the worst case).

The EIP 90 gas mechanic is introduced because without it, all current contracts that make calls would stop working as they use an expression like `msg.gas - 40` to determine how much gas to make a call with, relying on the gas cost of calls being 40. Additionally, EIP 114 is introduced because, given that we are making the cost of a call higher and less predictable, we have an opportunity to do it at no extra cost to currently available guarantees, and so we also achieve the benefit of replacing the call stack depth limit with a "softer" gas-based restriction, thereby eliminating call stack depth attacks as a class of attack that contract developers have to worry about and hence increasing contract programming safety. Note that with the given parameters, the de-facto maximum call stack depth is limited to ~340 (down from ~1024), mitigating the harm caused by any further potential quadratic-complexity DoS attacks that rely on calls.

The gas limit increase is recommended so as to preserve the de-facto transactions-per-second processing capability of the system for average contracts.


#eip-155.md
## Preamble
```
EIP: 155
Title: Simple replay attack protection
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-10-14
```

### Parameters
- `FORK_BLKNUM`: TBA
- `CHAIN_ID`: 1
### Specification

If `block.number >= FORK_BLKNUM` and `v = CHAIN_ID * 2 + 35` or `v = CHAIN_ID * 2 + 36`, then when computing the hash of a transaction for purposes of signing or recovering, instead of hashing only the first six elements (ie. nonce, gasprice, startgas, to, value, data), hash nine elements, with `v` replaced by `CHAIN_ID`, `r = 0` and `s = 0`. The currently existing signature scheme using `v = 27` and `v = 28` remains valid and continues to operate under the same rules as it does now.
### Example

Consider a transaction with `nonce = 9`, `gasprice = 20 * 10**9`, `startgas = 21000`, `to = 0x3535353535353535353535353535353535353535`, `value = 10**18`, `data=''` (empty).

The "signing data" becomes:

```
0xec098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a764000080018080
```

The "signing hash" becomes:

```
0xdaf5a779ae972f972197303d7b574746c7ef83eadac0f2791ad23db92e4c8e53
```

If the transaction is signed with the private key `0x4646464646464646464646464646464646464646464646464646464646464646`, then the v,r,s values become:

```
(37, 18515461264373351373200002665853028612451056578545711640558177340181847433846, 46948507304638947509940763649030358759909902576025900602547168820602576006531)
```

Notice the use of 37 instead of 27. The signed tx would become:

```
0xf86c098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a76400008025a028ef61340bd939bc2195fe537567866003e1a15d3c71ff63e1590620aa636276a067cbe9d8997f761aecb703304b3800ccf555c9f3dc64214b297fb1966a3b6d83
```
### Rationale

This would provide a way to send transactions that work on ethereum without working on ETC or the Morden testnet. ETC is encouraged to adopt this EIP but replacing `CHAIN_ID` with a different value, and all future testnets, consortium chains and alt-etherea are encouraged to adopt this EIP replacing `CHAIN_ID` with a unique value.


### List of Chain ID's:

| `CHAIN_ID`     | Chain(s)                                   |
| ---------------| -------------------------------------------|
| 1              | Ethereum mainnet                           |
| 2              | Morden (disused), Expanse mainnet          |
| 3              | Ropsten                                    |
| 4              | Rinkeby                                    |
| 30             | Rootstock mainnet                          |
| 31             | Rootstock testnet                          |
| 42             | Kovan                                      |
| 61             | Ethereum Classic mainnet                   |
| 62             | Ethereum Classic testnet                   |
| 1337           | Geth private chains (default)              |


#eip-158.md
```
EIP: 158
Title: State clearing
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Superseded
Created: 2016-10-16
Superseded-By: 161
```

# Specification

For all blocks where `block.number >= FORK_BLKNUM` (TBA):
1. In all cases where a state change is made to an account, and this state change results in the account state being saved with nonce = 0, balance = 0, code empty, storage empty (hereinafter "empty account"), the account is instead deleted.
2. If a address is "touched" and that address contains an empty account, then it is deleted. A "touch" is defined as any situation where if the account at the given address were nonexistent it would be created.
3. Whenever the EVM checks if an account exists, emptiness is treated as equivalent to nonexistence. Particularly, note that this implies that, once this change is enabled, there is no longer a meaningful difference between emptiness and nonexistence from the point of view of EVM execution.
4. Zero-value calls and zero-value suicides no longer consume the 25000 account creation gas cost in any circumstance

The cases where a "touch" takes place can be enumerated as follows:
- Zero-value-bearing CALLs
- CREATEs (if the code that is ultimately saved is empty and there is no ether remaining in the account when it is saved)
- Zero-value-bearing SUICIDEs
- Transaction recipients
- Contracts created in contract creation transactions
- Miners receiving transaction fees (note the case where the gasprice is zero, and the account does not yet exist because it only receives the block/uncle/nephew rewards _after_ processing every transaction)
### Specification (1b)

When the EVM checks for emptiness (for the purpose of possibly applying the 25000 gas cost), emptiness is defined by `is_empty(acct): return get_balance(acct) == 0 and get_code(acct) == "" and get_nonce(acct) == 0`; emptiness of storage does not matter. This simplifies client implementation because there is no need to add extra complexity to make caches enumerable in the correct way and does not significantly affect the intended result, as the cases where balance/code/nonce are empty but storage is nonempty where this change would lead to an extra 25000 gas being paid are pathological and have no real use value.
### Specification (1c)

Do not implement point 2 above (ie. no new empty accounts can be created, but existing ones are not automatically destroyed unless their state is actually _changed_). Instead, during each block starting from (and including) N and ending when there are no null accounts left, select the 1000 null accounts that are left-most in order of sha3(address), and delete them (ordering by hash is necessary so as to allow the accounts to be easily found by iterating the tree).
# Rationale

This removes a large number of empty accounts that have been put in the state at very low cost due to flaws in earlier versions of the Ethereum protocol, thereby greatly reducing state size and hence both reducing the hard disk load of a full client and reducing the time for a fast sync. Additionally, it simplifies the protocol in the long term, as once all "empty" objects are cleared out there is no longer any meaningful distinction between an account being empty and being nonexistent, and indeed one can simply view nonexistence as a compact representation of emptiness.

Note that this proposal does introduce a **temporary** breaking of existing guarantees, in that by repeatedly zero-value-calling already existing empty accounts one can create a state change at a cost of 700 gas per account instead of the usual 5000 per gas minimum (with SUICIDE refunds this goes down further to 350 gas per account). Allowing such a large number of state writes per block will lead to heightened block processing times and increase uncle rates in the short term while the existing empty accounts are being cleared, and eventually once all empty accounts are cleared this issue will no longer exist.

# References

1. EIP-158 issue and discussion: https://github.com/ethereum/EIPs/issues/158
2. EIP-161 issue and discussion: https://github.com/ethereum/EIPs/issues/161


#eip-161.md
```
EIP: 161
Title: State trie clearing (invariant-preserving alternative)
Author: Gavin Wood
Type: Standard Track
Category: Core
Status: Final
Created: 2016-10-24
```

# Specification

a. Account creation transactions and the `CREATE` operation SHALL, prior to the execution of the initialisation code, **increment** the **nonce** over and above its normal starting value by **one** (for normal networks, this will be simply 1, however test-nets with non-zero default starting nonces will be different).

b. Whereas `CALL` and `SUICIDE` would charge 25,000 gas when the destination is non-existent, now the charge SHALL **only** be levied if the operation transfers **more than zero value** and the destination account is _dead_.

c. No account may _change state_ from non-existent to existent-but-_empty_. If an operation would do this, the account SHALL instead remain non-existent.

d. _At the end of the transaction_, any account _touched_ by the execution of that transaction which is now _empty_ SHALL instead become non-existent (i.e. **deleted**).

Where:

An account is considered to be _touched_ when it is involved in any potentially _state-changing_ operation. This includes, but is not limited to, being the recipient of a **transfer of zero value**.

An account is considered _empty_ when it has **no code** and **zero nonce** and **zero balance**.

An account is considered _dead_ when either it is non-existent or it is _empty_.

_At the end of the transaction_ is immediately following the execution of the suicide list, prior to the determination of the state trie root for receipt population.

An account _changes state_ when:
- it is the target or refund of a `SUICIDE` operation for **zero or more** value;
- it is the source or destination of a `CALL` operation or message-call transaction transferring **zero or more** value;
- it is the source or newly-creation of a `CREATE` operation or contract-creation transaction endowing **zero or more** value;
- as the block author ("miner") it is recipient of block-rewards or transaction-fees of **zero or more**.

## Notes

In the present Ethereum protocol, it should be noted that very few state changes can ultimately result in accounts that are empty following the execution of the transaction. In fact there are only four contexts that current implementations need track:
- an empty account has zero value transferred to it through `CALL`;
- an empty account has zero value transferred to it through `SUICIDE`;
- an empty account has zero value transferred to it through a message-call transaction;
- an empty account has zero value transferred to it through a zero-gas-price fees transfer.

# Rationale

Same as #158 except that several edge cases are avoided since we do not break invariants:
- ~~that an account can go from having code and storage to not having code or storage mid-way through the execution of a transaction;~~ [corrected]
- that a newly created account cannot be deleted prior to being deployed.

`CREATE` avoids zero in the nonce to avoid any suggestion of the oddity of `CREATE`d accounts being reaped half-way through their creation.

# References

1. EIP-158 issue and discussion: https://github.com/ethereum/EIPs/issues/158
2. EIP-161 issue and discussion: https://github.com/ethereum/EIPs/issues/161


#eip-162.md
```
EIP: 162
Title: Initial ENS Hash Registrar
Author: Maurelian and Nick Johnson
Status: Final
Type: Informational
Created: 2016-10-25
```

## Contents
- Abstract
- Motivations
- Specification
  - Initial restrictions
  - Name format for hash registration
  - Auctioning names
  - Deeds
  - Deployment and Upgrade process
  - Registrar Interface
- Rationale
  - Not committing to a permanent registrar at the outset
  - Valid names >= 7 characters
  - Restricting TLD to `.eth`
  - Holding ether as collateral
- Prior work

<!-- /MarkdownTOC -->

## Abstract

This ERC describes the implementation, as deployed to the main ethereum network on 2017-05-04, of a registrar contract to govern the allocation of names in the Ethereum Name Service (ENS). The corresponding source code is [here](https://github.com/ethereum/ens/blob/mainnet/contracts/HashRegistrarSimplified.sol).

For more background, refer to [EIP 137](https://github.com/ethereum/EIPs/issues/137).

> Registrars are responsible for allocating domain names to users of the system, and are the only entities capable of updating the ENS; the owner of a node in the ENS registry is its registrar. Registrars may be contracts or externally owned accounts, though it is expected that the root and top-level registrars, at a minimum, will be implemented as contracts.
>
> \- EIP 137

A well designed and governed registrar is essential to the success of the ENS described in EIP 137, but is described separately in this document as it is external to the core ENS protocol.

In order to maximize utility and adoption of a new namespace, the registrar should mitigate speculation and "name squatting", however the best approach for mitigation is unclear. Thus an "initial" registrar is proposed, which implements a simple approach to name allocation. During the initial period, the available namespace will be significantly restricted to the `.eth` top level domain, and subdomain shorter than 7 characters in length disallowed. This specification largely describes @alexvandesande and @arachnid's [hash registrar implementation](https://github.com/Arachnid/ens/blob/master/HashRegistrarSimplified.sol) in order to facilitate discussion.

The intent is to replace the Initial Registrar contract with a permanent registrar contract. The Permanent Registrar will increase the available namespace, and incorporate lessons learned from the performance of the Initial Registrar. This upgrade is expected to take place within approximately 2 years of initial deployment.

## Motivations

The following factors should be considered in order to optimize for adoption of the ENS, and good governance of the Initial Registrar's namespace.

**Upgradability:** The Initial Registrar should be safely upgradeable, so that knowledge gained during its deployment can be used to replace it with an improved and permanent registrar.

**Effective allocation:** Newly released namespaces often create a land grab situation, resulting in many potentially valuable names being purchased but unused, with the hope of re-selling at a profit. This reduces the availability of the most useful names, in turn decreasing the utility of the name service to end users.

Achieving an effective allocation may or may not require human intervention for dispute resolution and other forms of curation. The Initial Registrar should not aim to create to most effective possible allocation, but instead limit the cost of misallocation in the long term.

**Security:** The registrar will hold a balance of ether without an explicit limit. It must be designed securely.

**Simplicity:** The ENS specification itself emphasizes a separation of concerns, allowing the most essential element, the registry to be as simple as possible. The interim registrar in turn should be as simple as possible while still meeting its other design goals.

**Adoption:** Successful standards become more successful due to network effects. The registrar should consider what strategies will encourage the adoption of the ENS in general, and the namespace it controls in particular.

## Specification

### Initial restrictions

The Initial Registrar is expected to be in service for approximately two years, prior to upgrading. This should be sufficient time to learn, observe, and design an updated system.

During the initial two year period, the available name space will be restricted to the `.eth` TLD.

This restriction is enforced by the owner of the ENS root node who should not assign any nodes other than `.eth` to the Initial Registrar. The ENS's root node should be controlled by multiple parties using a multisig contract.

The Initial Registrar will also prohibit registration of names 6 characters or less in length.

### Name format for hash registration

Names submitted to the initial registrar must be hashed using Ethereum's sha3 function. Note that the hashes submitted to the registrar are the hash of the subdomain label being registered, not the namehash as defined in EIP 137.

For example, in order to register `abcdefg.eth`, one should submit `sha3('abcdefg')`, not `sha3(sha3(0, 'eth'), 'abcdefg')`.

### Auctioning names

The registrar will allocate the available names through a Vickrey auction:

> A Vickrey auction is a type of sealed-bid auction. Bidders submit written bids without knowing the bid of the other people in the auction. The highest bidder wins but the price paid is the second-highest bid. This type of auction... gives bidders an incentive to bid their true value.
>
> \- [Vickrey Auction, Wikipedia](https://en.wikipedia.org/wiki/Vickrey_auction)

The auction lifecycle of a name has 5 possible states, or Modes.

1. **Not-yet-available:** The majority of names will be initially unavailable for auction, and will become available some time during the 8 weeks after launch.
2. **Open:** The earliest availability for a name is determined by the most significant byte of its sha3 hash. `0x00` would become available immediately, `0xFF` would become available after 8 weeks, and the availability of other names is distributed accordingly. Once a name is available, it is possible to start an auction on it.
3. **Auction:** Once the auction for a name has begun, there is a 72 hour bidding period. Bidders must submit a payment of ether, along with sealed bids as a hash of `sha3(bytes32 hash, address owner, uint value, bytes32 salt)`. The bidder may obfuscate the true bid value by sending a greater amount of ether.
4. **Reveal:** After the bidding period, a 48 hour reveal period commences. During this time, bidders must reveal the true parameters of their sealed bid. As bids are revealed, ether payments are returned according to the schedule of "refund ratios" outlined in the table below. If no bids are revealed, the name will return to the Open state.
5. **Owned:** After the reveal period has finished, the winning bidder must submit a transaction to finalize the auction, which then calls the ENS's `setSubnodeOwner` function, recording the winning bidder's address as the owner of the hash of the name.

The following table outlines important parameters which define the Registrar's auction mechanism.

#### Registrar Parameters

|        Name        |                                            Description                                             |   Value    |
|--------------------|----------------------------------------------------------------------------------------------------|------------|
| totalAuctionLength | The full time period from start of auction to end of the reveal period.                            | 5 days     |
| revealPeriod       | The length of the time period during which bidding is no longer allowed, and bids must be revealed. | 48 hours   |
| launchLength       | The time period during which all names will become available for auction.                          | 8 weeks    |
| minPrice           | The minimum amount of ether which must be locked up in exchange for ownership of a name.           | 0.01 ether |

### Deeds

The Initial Registrar contract does not hold a balance itself. All ether sent to the Registrar will be held in a separate `Deed` contracts. A deed contract is first created and funded when a sealed bid is submitted. After an auction is completed and a hash is registered, the deed for the winning bid is held in exchange for ownership of the hash. Non-winning bids are refunded.

A deed for an owned name may be transferred to another account by its owner, thus transferring ownership and control of the name.

After 1 year of registration, the owner of a hash may choose to relinquish ownership and have the value of the deed returned to them.

Deeds for non-winning bids can be closed by various methods, at which time any ether held will either be returned to the bidder, burnt, or sent to someone else as a reward for actions which help the registrar.

The following table outlines what portion of the balance held in a deed contract will be returned upon closure, and to whom. The remaining balance will be burnt.

#### Refund schedule

| Reason for Deed closure | Refund Recipient | Refund Percentage |
| --- | --- | --- |
| A valid non-winning bid is revealed. | Bidder | 99.5% |
| A bid submitted after the auction period is revealed. | Bidder | 99.5% |
| A bid is revealed after the reveal period. <sup>1</sup> | Bidder | 0.5% |
| An expired sealed bid is cancelled. <sup>2</sup> | Canceler | 0.5% |
| A registered hash is reported as invalid. <sup>3</sup> | Reporter | 50% |
| A registered hash is reported as invalid. <sup>3</sup> | Owner | 50% |

##### Notes:

1. This incentivizes all bids to be revealed in time. If bids could be revealed late, an extortion attack on the current highest bidder could be made by threatening to reveal a new second highest bid.
2. A bid which remains sealed after more than 2 weeks and 5 days may be cancelled by anyone to collect a small reward.
2. Since names are hashed before auctioning and registration, the Initial Registrar is unable to enforce character length restrictions independently. A reward is therefore provided for reporting invalid names.

### Deployment and Upgrade process

The Initial Registrar requires the ENS's address as a contructor, and should be deployed after the ENS. The multisig account owning the root node in the ENS should then set the Initial Registrar's address as owner of the `eth` node.

The Initial Registrar is expected to be replaced by a Permanent Registrar approximately 2 years after deployment. The following process should be used for the upgrade:
1. The Permanent Registrar contract will be deployed.
2. The multisig account owning the root node in the ENS will assign ownership of the `.eth` node to the Permanent Registrar.
3. Owners of hashes in the Initial Registrar will be responsible for registering their deeds to the Permanent Registrar. A couple options are considered here:
   1. Require owners to transfer their ownership prior to a cutoff date in order to maintain ownership and/or continue name resolution services.
   2. Have the Permanent Registrar query the Initial Registrar for ownership if it is lacking an entry.

### Planned deactivation

In order to limit dependence on the Initial Registrar, new auctions will stop after 4 years, and all ether held in deeds after 8 years will become unreachable.

### Registrar Interface

`function state(bytes32 _hash) constant returns (Mode)`
- Implements a state machine returning the current state of a name

`function entries(bytes32 _hash) constant returns (Mode, address, uint, uint, uint)`
- Returns the following information regarding a registered name:
  * state
  * deed address
  * registration date
  * balance of the deed
  * highest value bid at auction

`function getAllowedTime(bytes32 _hash) constant returns (uint timestamp)`
- Returns the time at which the hash will no longer be in the initial `not-yet-available` state.

`function isAllowed(bytes32 _hash, uint _timestamp) constant returns (bool allowed)`
- Takes a hash and a time, returns true if and only if it has passed the initial `not-yet-available` state.

`function startAuction(bytes32 _hash);`
- Moves the state of a hash from Open to Auction. Throws if state is not Open.

`function startAuctions(bytes32[] _hashes);`
- Starts multiple auctions on an array of hashes. This enables someone to open up an auction for a number of dummy hashes when they are only really interested in bidding for one. This will increase the cost for an attacker to simply bid blindly on all new auctions. Dummy auctions that are open but not bid on are closed after a week.

`function shaBid(bytes32 hash, address owner, uint value, bytes32 salt) constant returns (bytes32 sealedBid);`
- Takes the parameters of a bid, and returns the sealedBid hash value required to participate in the bidding for an auction. This obfuscates the parameters in order to mimic the mechanics of placing a bid in an envelope.

`function newBid(bytes32 sealedBid);`
- Bids are sent by sending a message to the main contract with a sealedBid hash and an amount of ether. The hash contains information about the bid, including the bidded name hash, the bid value, and a random salt. Bids are not tied to any one auction until they are revealed. The value of the bid itself can be masqueraded by sending more than the value of your actual bid. This is followed by a 48h reveal period. Bids revealed after this period will be burned and the ether unrecoverable. Since this is an auction, it is expected that most public hashes, like known domains and common dictionary  words, will have multiple bidders pushing the price up.

`function startAuctionsAndBid(bytes32[] hashes, bytes32 sealedBid)`
- A utility function allowing a call to `startAuctions` followed by `newBid` in a single transaction.


`function unsealBid(bytes32 _hash, address _owner, uint _value, bytes32 _salt);`
- Once the bidding period is completed, there is a reveal period during with the properties of a bid are submitted to reveal them. The registrar hashes these properties using the `shaBid()` function above to verify that they match a pre-existing sealed bid. If the unsealedBid is the new best bid, the old best bid is returned to its bidder.

`function cancelBid(bytes32 seal);`
- Cancels an unrevealed bid according to the rules described in the notes on the refund schedule above.

`function finalizeAuction(bytes32 _hash);`

After the registration date has passed, this function can be called to finalize the auction, which then calls the ENS function `setSubnodeOwner()`  updating the ENS record to set the winning bidder as owner of the node.

`function transfer(bytes32 _hash, address newOwner);`
- Update the owner of the ENS node corresponding to the submitted hash to a new owner. This function must be callable only by the current owner.

`function releaseDeed(bytes32 _hash);`
- After some time, the owner can release the property and get their ether back.

`function invalidateName(string unhashedName);`
- Since registration is done on the hash of a name, the registrar itself cannot validate names. This function can be used to report a name which is 6 characters long or less. If it has been registered, the submitter will earn 10% of the deed value. We are purposefully handicapping the simplified registrar as a way to force it into being restructured in a few years.

`function eraseNode(bytes32[] labels)`
- Allows anyone to delete the owner and resolver records for a subdomain of a name that is not currently owned in the registrar. For instance, to zero `foo.bar.eth` on a registrar that owns `.eth`, pass an array containing `[sha3('foo'), sha3('bar')]`.

`function transferRegistrars(bytes32 _hash) onlyOwner(_hash);`
- Used during the upgrade process to a permanent registrar. If this registrar is no longer the owner of the its root node in the ENS, this function will transfers the deed to the current owner, which should be a new registrar. This function throws if this registrar still owns its root node.

## Rationale

### Starting with a temporary registrar

Anticipating and designing for all the potential issues of name allocation names is unlikely to succeed. This approach chooses not to be concerned with getting it perfect, but allows us to observe and learn with training wheels on, and implement improvements before expanding the available namespace to shorter names or another TLD.

### Valid names >= 7 characters

Preserving the shortest, and often most valuable, domain names for the upgraded registrar provides the opportunity to implement processes for dispute resolution (assuming they are found to be necessary).

### Delayed release of names

A slower release allows for extra time to identify, and address any issues which may arise after launch.

### Restricting TLD to `.eth`

Choosing a single TLD helps to maximize network effects by focusing on one namespace.

A three letter TLD is a pattern made familiar by it's common usage in internet domain names. This familiarity significantly increases the potential of the ENS to be integrated into pre-existing DNS systems, and reserved as a [special-use domain name](http://www.iana.org/assignments/special-use-domain-names/special-use-domain-names.xhtml#special-use-domain).  A recent precedent for this is the [reservation of the `.onion` domain](https://tools.ietf.org/html/rfc7686).

### Holding ether as collateral

This approach is simpler than the familiar model of requiring owners to make recurring payments to retain ownership of a domain name. It also makes the initial registrar a revenue neutral service.

## Prior work

This document borrows heavily from several sources:
- [EIP 137](https://github.com/ethereum/EIPs/issues/137) outlines the initial implementation of the Registry Contract (ENS.sol) and associated Resolver contracts.
- [ERC 26](https://github.com/ethereum/EIPs/issues/26) was the first ERC to propose a name service at the contract layer
- @alexvandesande's current implementation of the [HashRegistrar](https://github.com/Arachnid/ens/blob/master/HashRegistrarSimplified.sol)

### Edits:
- 2016-10-26 Added link Alex's design in abstract
- 2016-11-01 change 'Planned deactivation' to h3'
- 2017-03-13 Update timelines for bidding and reveal periods


#eip-170.md
```
EIP: 170
Title: Contract code size limit
Author: Vitalik Buterin
Type: Standard Track
Category: Core
Status: Final
Created: 2016-11-04
```

### Specification

If `block.number >= FORK_BLKNUM`, then if contract creation initialization returns data with length of **more than** `0x6000` (`2**14 + 2**13`) bytes, contract creation fails with an out of gas error.

### Rationale

Currently, there remains one slight quadratic vulnerability in ethereum: when a contract is called, even though the call takes a constant amount of gas, the call can trigger O(n) cost in terms of reading the code from disk, preprocessing the code for VM execution, and also adding O(n) data to the Merkle proof for the block's proof-of-validity. At current gas levels, this is acceptable even if suboptimal. At the higher gas levels that could be triggered in the future, possibly very soon due to dynamic gas limit rules, this would become a greater concern - not nearly as serious as recent denial of service attacks, but still inconvenient especially for future light clients verifying proofs of validity or invalidity. The solution is to put a hard cap on the size of an object that can be saved to the blockchain, and do so non-disruptively by setting the cap at a value slightly higher than what is feasible with current gas limits.

### References

1. EIP-170 issue and discussion: https://github.com/ethereum/EIPs/issues/170
2. pyethereum implementation: https://github.com/ethereum/pyethereum/blob/5217294871283d8dc4fb3ca9d8a78c7d416490e8/ethereum/messages.py#L397


#eip-181.md
<pre>
  EIP: 181
  Title: ENS support for reverse resolution of Ethereum addresses
  Author: Nick Johnson <arachnid@notdot.net>
  Status: Final
  Type: Standard Track
  Category: ERC
  Created: 2016-12-01
</pre>

# Abstract
This EIP specifies a TLD, registrar, and resolver interface for reverse resolution of Ethereum addresses using ENS. This permits associating a human-readable name with any Ethereum blockchain address. Resolvers can be certain that the reverse record was published by the owner of the Ethereum address in question.

# Motivation
While name services are mostly used for forward resolution - going from human-readable identifiers to machine-readable ones - there are many use-cases in which reverse resolution is useful as well:

 - Applications that allow users to monitor accounts benefit from showing the name of an account instead of its address, even if it was originally added by address.
 - Attaching metadata such as descriptive information to an address allows retrieving this information regardless of how the address was originally discovered.
 - Anyone can configure a name to resolve to an address, regardless of ownership of that address. Reverse records allow the owner of an address to claim a name as authoritative for that address.

# Specification
Reverse ENS records are stored in the ENS hierarchy in the same fashion as regular records, under a reserved domain, `addr.reverse`. To generate the ENS name for a given account's reverse records, convert the account to hexadecimal representation in lower-case, and append `addr.reverse`. For instance, the ENS registry's address at `0x112234455c3a32fd11230c42e7bccd4a84e02010` has any reverse records stored at `112234455c3a32fd11230c42e7bccd4a84e02010.addr.reverse`.

Note that this means that contracts wanting to do dynamic reverse resolution of addresses will need to perform hex encoding in the contract.

## Registrar
The owner of the `addr.reverse` domain will be a registrar that permits the caller to take ownership of 
the reverse record for their own address. It provides the following method:

    function claim(address owner) returns (bytes32 node);

When called by account `x` it will instruct the ENS registry to transfer ownership of the name `hex(x) + '.addr.reverse'` to the provided address, and return the namehash of the ENS record thus transferred.

Allowing the caller to specify an owner other than themselves for the relevant node facilitates contracts that need accurate reverse ENS entries delegating this to their creators with a minimum of code inside their constructor:

    reverseRegistrar.claim(msg.sender)

## Resolver interface
A new resolver interface is defined, consisting of the following method:

    function name(bytes32 node) constant returns (string);

Resolvers that implement this interface must return a valid ENS name for the requested node, or the empty string if no name is defined for the requested node.

The interface ID of this interface is 0x691f3431.

Future EIPs may specify more record types appropriate to reverse ENS records.

# Appendix 1: Registrar implementation

This registrar, written in Solidity, implements the specifications outlined above.

    pragma solidity ^0.4.0;

    import 'interface.sol';

    contract ReverseRegistrar {
        AbstractENS public ens;
        bytes32 public rootNode;
        
        /**
         * @dev Constructor
         * @param ensAddr The address of the ENS registry.
         * @param node The node hash that this registrar governs.
         */
        function ReverseRegistrar(address ensAddr, bytes32 node) {
            ens = AbstractENS(ensAddr);
            rootNode = node;
        }
    
        /**
         * @dev Transfers ownership of the reverse ENS record associated with the
         *      calling account.
         * @param owner The address to set as the owner of the reverse record in ENS.
         * @return The ENS node hash of the reverse record.
         */
        function claim(address owner) returns (bytes32 node) {
            var label = sha3HexAddress(msg.sender);
            ens.setSubnodeOwner(rootNode, label, owner);
            return sha3(rootNode, label);
        }
    
        /**
         * @dev An optimised function to compute the sha3 of the lower-case
         *      hexadecimal representation of an Ethereum address.
         * @param addr The address to hash
         * @return The SHA3 hash of the lower-case hexadecimal encoding of the
         *         input address.
         */
        function sha3HexAddress(address addr) constant returns (bytes32 ret) {
            assembly {
                let lookup := 0x3031323334353637383961626364656600000000000000000000000000000000
                let i := 40
            loop:
                i := sub(i, 1)
                mstore8(i, byte(and(addr, 0xf), lookup))
                addr := div(addr, 0x10)
                i := sub(i, 1)
                mstore8(i, byte(and(addr, 0xf), lookup))
                addr := div(addr, 0x10)
                jumpi(loop, i)
                ret := sha3(0, 40)
            }
        }
    }


#eip-190.md
```
EIP: Draft
Title: Ethereum Smart Contract Packaging Standard
Authors: Piper Merriam, Tim Coulter, Denis Erfurt (mhhf), RJ Catalano (VoR0220), Iuri Matias (iurimatias)
Status: Draft
Type: Standards Track - ERC
Created: 2017-01-10
```

# Abstract

This ERC proposes a specification for Ethereum smart contract packages.  

The specification was collaboratively developed by the following Ethereum development framework maintainers.

* Tim Coulter (Truffle)
* Denis Erfurt (Dapple)
* Piper Merriam (Populus)
* RJ Catalano (Eris PM)
* Iuri Matias (Embark)

# Motivation

Packaging is a core piece of modern software development which is missing from the Ethereum ecosystem.  The lack of packaging limits the ability for developers to reuse code which negatively affects productivity and security.

A key example of this is the ERC20 standard.  There are a few well audited reusable token contracts available but most developers end up writing their own because of the difficulty in finding and reusing existing code.

A packaging standard should have the following positive effects on the ecosystem:

* Greater overall productivity caused by the ability to reuse existing code.
* Increased security caused by the ability to reuse existing well audited implementations of common patterns (ERC20, crowdfunding, etc).

Smart contract packaging should also have a direct positive effect on the end user.  Wallet software will be able to consume a released package and generate an interface for interacting with any deployed contracts included within that package.  With the advent of [ENS](https://github.com/ethereum/EIPs/issues/137) all of the pieces will be in place for a wallet to take a human readable name and present the user with an interface for interacting with the underlying application.


# Specification

The full specification for this standard is maintained separately in the repository [epm/epm-spec](https://github.com/ethpm/epm-spec).

This EIP refers to the `1.0.0` version of the specification: [https://github.com/ethpm/epm-spec/tree/v1.0.0](https://github.com/ethpm/epm-spec/tree/v1.0.0) 

The specification contains details for a single document referred to as a *"Release Lockfile"*.  

* Release Lockfile Specification: [https://github.com/ethpm/epm-spec/blob/v1.0.0/release-lockfile.spec.md](https://github.com/ethpm/epm-spec/blob/v1.0.0/release-lockfile.spec.md).
* JSON Schema for Release Lockfile: [https://github.com/ethpm/epm-spec/blob/v1.0.0/spec/release-lockfile.spec.json](https://github.com/ethpm/epm-spec/blob/v1.0.0/spec/release-lockfile.spec.json)

> These documents have not been inlined into this ERC to ensure that there is a single source of truth for the specification.


# Use Cases

This specification covers the following types of smart contract packages.

1. Packages with contracts intended to be used as base contract such as the common `owned` pattern.
2. Packages with contracts that are ready to use as-is such as an ERC20 token contract.
3. Packages with deployed contracts such as libraries or services.

Full explanations and examples of these use cases can be found in the [`README.md`](https://github.com/ethpm/epm-spec/blob/v1.0.0/README.md#use-cases) from the `epm/epm-spec` repository.


# Package Managers

The *Release Lockfile* is intended for consumption by package management software.  Specific care was made to ensure that all of the following functionality can be implemented by package managers.


## Deterministic builds

Ensures that a package will always resolve to the same set of dependencies and source files.  Both source files and dependencies are content addressed to ensure that the referenced resources cannot change.


## Bytecode verification

Contains the appropriate information for a package manager to inspect a deployed contract and verify that its bytecode matches the bytecode that results from compilation and linking of the package source code.


## Multi-chain deploys

Supports deployments across multiple chains, allowing a package to define addresses on both the public mainnet and testnet.


## Trusted packages

Allows for packages which exclude source code or other elements which would be needed for verification of the contract bytecode.  This allows for minimalistic packages to be created for special situations where the package manager will not be performing verification.


# Framework support and integration

Support for ERC190 is either implemented or in progress for the following:

* [Truffle](http://truffleframework.com/)
* [Populus](http://populus.readthedocs.io/en/latest/)
* [Dapple](http://dapple.readthedocs.io/en/master/)
* [Eris PM](https://github.com/eris-ltd/eris-cli)
* [Embark](https://github.com/iurimatias/embark-framework)
* [Browser Solidity](https://github.com/ethereum/browser-solidity/issues/386)


#eip-2.md
```
EIP: 2
Title: Homestead Hard-fork Changes
Author: Vitalik Buterin <v@buterin.com>
Status: Final
Type: Standard Track
Category: Core
Created: 2015-11-15
```

# Specification

If `block.number >= HOMESTEAD_FORK_BLKNUM` (e.g., 1.150.000 on livenet, 494.000 on Morden and 0 on future testnets), do the following:

1. The gas cost *for creating contracts via a transaction* is increased from 21000 to 53000, ie. if you send a transaction and the to address is the empty string, the initial gas subtracted is 53000 plus the gas cost of the tx data, rather than 21000 as is currently the case. Contract creation from a contract using the `CREATE` opcode is unaffected.
2. All transaction signatures whose s-value is greater than `secp256k1n/2` are now considered invalid. The ECDSA recover precompiled contract remains unchanged and will keep accepting high s-values - this is useful if e.g. a contract recovers old Bitcoin signatures.
3. If contract creation does not have enough gas to pay for the final gas fee for adding the contract code to the state, the contract creation fails (ie. goes out-of-gas) rather than leaving an empty contract.
4. Change the difficulty adjustment algorithm from the current formula: `block_diff = parent_diff + parent_diff // 2048 * (1 if block_timestamp - parent_timestamp < 13 else -1) + int(2**((block.number // 100000) - 2))` (where the ` + int(2**((block.number // 100000) - 2))` represents the exponential difficulty adjustment component) to `block_diff = parent_diff + parent_diff // 2048 * max(1 - (block_timestamp - parent_timestamp) // 10, -99) + int(2**((block.number // 100000) - 2))`, where `//` is the integer division operator, eg. `6 // 2 = 3`, `7 // 2 = 3`, `8 // 2 = 4`. The `minDifficulty` still defines the minimum difficulty allowed and no adjustment may take it below this.

# Rationale

Currently, there is an excess incentive to create contracts via transactions, where the cost is 21000, rather than contracts, where the cost is 32000. Additionally, with the help of suicide refunds, it is currently possible to make a simple ether value transfer using only 11664 gas; the code for doing this is as follows:

```python
from ethereum import tester as t
> from ethereum import utils
> s = t.state()
> c = s.abi_contract('def init():\n suicide(0x47e25df8822538a8596b28c637896b4d143c351e)', endowment=10**15)
> s.block.get_receipts()[-1].gas_used
11664
> s.block.get_balance(utils.normalize_address(0x47e25df8822538a8596b28c637896b4d143c351e))
1000000000000000
```
This is not a particularly serious problem, but is nevertheless arguably a bug.

Allowing transactions with any s value with `0 < s < secp256k1n`, as is currently the case, opens a transaction malleability concern, as one can take any transaction, flip the s value from `s` to `secp256k1n - s`, flip the v value (`27 -> 28`, `28 -> 27`), and the resulting signature would still be valid. This is not a serious security flaw, especially since Ethereum uses addresses and not transaction hashes as the input to an ether value transfer or other transaction, but it nevertheless creates a UI inconvenience as an attacker can cause the transaction that gets confirmed in a block to have a different hash from the transaction that any user sends, interfering with user interfaces that use transaction hashes as tracking IDs. Preventing high s values removes this problem.

Making contract creation go out-of-gas if there is not enough gas to pay for the final gas fee has the benefits that (i) it creates a more intuitive "success or fail" distinction in the result of a contract creation process, rather than the current "success, fail, or empty contract" trichotomy, (ii) makes failures more easily detectable, as unless contract creation fully succeeds then no contract account will be created at all, and (iii) makes contract creation safer in the case where there is an endowment, as there is a guarantee that either the entire initiation process happens or the transaction fails and the endowment is refunded.

The difficulty adjustment change conclusively solves a problem that the Ethereum protocol saw two months ago where an excessive number of miners were mining blocks that contain a timestamp equal to `parent_timestamp + 1`; this skewed the block time distribution, and so the current block time algorithm, which targets a *median* of 13 seconds, continued to target the same median but the mean started increasing. If 51% of miners had started mining blocks in this way, the mean would have increased to infinity. The proposed new formula is roughly based on targeting the mean; one can prove that with the formula in use an average block time longer than 24 seconds is mathematically impossible in the long term.

The use of `(block_timestamp - parent_timestamp) // 10` as the main input variable rather than the time difference directly serves to maintain the coarse-grained nature of the algorithm, preventing an excessive incentive to set the timestamp difference to exactly 1 in order to create a block that has slightly higher difficulty and that will thus be guaranteed to beat out any possible forks. The cap of -99 simply serves to ensure that the difficulty does not fall extremely far if two blocks happen to be very far apart in time due to a client security bug or other black-swan issue.

# Implementation

This is implemented in Python here:

1. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L130
2. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L129
3. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/processblock.py#L304
4. https://github.com/ethereum/pyethereum/blob/d117c8f3fd93359fc641fd850fa799436f7c43b5/ethereum/blocks.py#L42


#eip-5.md
### Title

      EIP: 5
      Title: Gas Usage for `RETURN` and `CALL*`
      Author: Christian Reitwiessner <c@ethdev.com>
      Status: Draft
      Type: Standards Track
      Layer: Consensus (hard-fork)
      Created: 2015-11-22

### Abstract

This EIP makes it possible to call functions that return strings and other dynamically-sized arrays.
Currently, when another contract / function is called from inside the Ethereum Virtual Machine,
the size of the output has to be specified in advance. It is of course possible to give a larger
size, but gas also has to be paid for memory that is not written to, which makes returning
dynamically-sized data both costly and inflexible to the extent that it is actually unusable.

The solution proposed in this EIP is to charge gas only for memory that is actually written to at
the time the `CALL` returns.

### Specification

The gas and memory semantics for `CALL`, `CALLCODE` and `DELEGATECALL` (called later as `CALL*`)
are changed in the following way (`CREATE` does not write to memory and is thus unaffected):

Suppose the arguments to `CALL*` are `gas, address, value, input_start, input_size, output_start, output_size`,
then, at the beginning of the opcode, gas for growing memory is only charged for `input_start + input_size`, but not
for `output_start + output_size`.

If the called contract returns data of size `n`, the memory of the calling contract is grown to
`output_start + min(output_size, n)` (and the calling contract is charged gas for that) and the
output is written to the area `[output_start, output_start + min(n, output_size))`.

The calling contract can run out of gas both at the beginning of the opcode and at the end
of the opcode.

After the call, the `MSIZE` opcode should return the size the memory was actually grown to.

### Motivation

In general, it is good practise to reserve a certain memory area for the output of a call,
because letting a subroutine write to arbitrary areas in memory might be dangerous. On the
other hand, it is often hard to know the output size of a call prior to performing the call:
The data could be in the storage of another contract which is generally inaccessible and
determining its size would require another call to that contract.

Furthermore, charging gas for areas of memory that are not actually written to is unnecessary.

This proposal tries to solve both problems: A caller can choose to provide a gigantic area of
memory at the end of their memory area. The callee can "write" to it by returning and the
caller is only charged for the memory area that is actually written.

This makes it possible to return dynamic data like strings and dynamically-sized arrays
in a very flexible way. It is even possible to determine the size of the returned data:
If the caller uses `output_start = MSIZE` and `output_size = 2**256-1`, the area of
memory that was actually written to is `(output_start, MSIZE)` (here, `MSIZE` as evaluated
after the call). This is important because it allows "proxy" contracts
which call other contracts whose interface they do not know and just return their output,
i.e. they both forward the input and the output. For this, it is important that the caller
(1) does not need to know the size of the output in advance and (2) can determine the
size of the output after the call.


### Rationale

This way of dealing with the problem requires a minimal change to the Ethereum Virtual Machine.
Other means of achieving a similar goal would have changed the opcodes themselves or
the number of their arguments. Another possibility would have been to only change the
gas mechanics if `output_size` is equal to `2**256-1`. Since the main difficulty in the
implementation is that memory has to be enlarged at two points in the code around `CALL`,
this would not have been a simplification.

At an earlier stage, it was proposed to also add the size of the returned data on the stack,
but the `MSIZE` mechanism described above should be sufficient and is much better
backwards compatible.

Some comments are available at https://github.com/ethereum/EIPs/issues/8

### Backwards Compatibility

This proposal changes the semantics of contracts because contracts can access the gas counter
and the size of memory.

On the other hand, it is unlikely that existing contracts will suffer from this change due to
the following reasons:

Gas:

The VM will not charge more gas than before. Usually, contracts are written in a way such
that their semantics do not change if they use up less gas. If more gas were used, contracts
might go out-of-gas if they perform a tight estimation for gas needed by sub-calls. Here,
contracts might only return more gas to their callers.

Memory size:

The `MSIZE` opcode is typically used to allocate memory at a previously unused spot.
The change in semantics affects existing contracts in two ways:

1. Overlaps in allocated memory. By using `CALL`, a contract might have wanted to allocate
   a certain slice of memory, even if that is not written to by the called contract.
   Subsequent uses of `MSIZE` to allocate memory might overlap with this slice that is
   now smaller than before the change. It is though unlikely that such contracts exist.

2. Memory addresses change. Rather general, if memory is allocated using `MSIZE`, the
   addresses of objects in memory will be different after the change. Contract should
   all be written in a way, though, such that objects in memory are _relocatable_,
   i.e. their absolute position in memory and their relative position to other
   objects does not matter. This is of course not the case for arrays, but they
   are allocated in a single allocation and not with an intermidiate `CALL`.


### Implementation

VM implementers should take care not to grow the memory until the end of the call and after a check that sufficient
gas is still available. Typical uses of the EIP include "reserving" `2**256-1` bytes of memory for the output.

Python implementation:

  old: http://vitalik.ca/files/old.py
  new: http://vitalik.ca/files/new.py


#eip-55.md
```
EIP: 55
Title: Mixed-case checksum address encoding
Author: Vitalik Buterin
Type: Standard Track
Category: ERC
Status: Accepted
Created: 2016-01-14
```

# Specification

Code:

``` python
from ethereum import utils

def checksum_encode(addr): # Takes a 20-byte binary address as input
    o = ''
    v = utils.big_endian_to_int(utils.sha3(addr.hex()))
    for i, c in enumerate(addr.hex()):
        if c in '0123456789':
            o += c
        else:
            o += c.upper() if (v & (2**(255 - 4*i))) else c.lower()
    return '0x'+o

def test(addrstr):
    assert(addrstr == checksum_encode2(bytes.fromhex(addrstr[2:])))

test('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed')
test('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
test('0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB')
test('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb')

```

In English, convert the address to hex, but if the `i`th digit is a letter (ie. it's one of `abcdef`) print it in uppercase if the `4*i`th bit of the hash of the lowercase hexadecimal address is 1 otherwise print it in lowercase.

# Implementation

In javascript:

```js
const createKeccakHash = require('keccak')

function toChecksumAddress (address) {
  address = address.toLowerCase().replace('0x','');
  var hash = createKeccakHash('keccak256').update(address).digest('hex')
  var ret = '0x'

  for (var i = 0; i < address.length; i++) {
    if (parseInt(hash[i], 16) >= 8) {
      ret += address[i].toUpperCase()
    } else {
      ret += address[i]
    }
  }

  return ret
}
```

```
> toChecksumAddress('0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359')
'0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359'
```

Note that the input to the Keccak256 hash is the lowercase hexadecimal string (i.e. the hex address encoded as ASCII):

```
    var hash = createKeccakHash('keccak256').update(Buffer.from(address.toLowerCase(), 'ascii')).digest()
```

# Rationale

Benefits:
- Backwards compatible with many hex parsers that accept mixed case, allowing it to be easily introduced over time
- Keeps the length at 40 characters
- On average there will be 15 check bits per address, and the net probability that a randomly generated address if mistyped will accidentally pass a check is 0.0247%. This is a ~50x improvement over ICAP, but not as good as a 4-byte check code.

# Adoption

| Wallet                   | displays checksummed addresses | rejects invalid mixed-case | rejects too short | rejects too long |
|--------------------------|--------------------------------|----------------------------|-------------------|------------------|
| Jaxx 1.2.17              | No                             | Yes                        | Yes               | Yes              |
| MetaMask 3.7.8           | Yes                            | Yes                        | Yes               | Yes              |
| Mist 0.8.10              | Yes                            | Yes                        | Yes               | Yes              |
| MyEtherWallet v3.9.4     | Yes                            | Yes                        | Yes               | Yes              |
| Parity 1.6.6-beta (UI)   | Yes                            | Yes                        | Yes               | Yes              |

### Exchange support for mixed-case address checksums, as of 2017-05-27:

| Exchange     | displays checksummed deposit addresses | rejects invalid mixed-case | rejects too short | rejects too long |
|--------------|----------------------------------------|----------------------------|-------------------|------------------|
| Bitfinex     | No                                     | Yes                        | Yes               | Yes              |
| Coinbase     | Yes                                    | No                         | Yes               | Yes              |
| GDAX         | Yes                                    | Yes                        | Yes               | Yes              |
| Kraken       | No                                     | No                         | Yes               | Yes              |
| Poloniex     | No                                     | No                         | Yes               | Yes              |
| Shapeshift   | No                                     | No                         | Yes               | Yes              |

# References

1. EIP 55 issue and discussion https://github.com/ethereum/eips/issues/55
2. Python example by @Recmo https://github.com/ethereum/eips/issues/55#issuecomment-261521584
3. Python implementation in [`ethereum-utils`](https://github.com/pipermerriam/ethereum-utils#to_checksum_addressvalue---text)
4. Ethereumjs-util implementation https://github.com/ethereumjs/ethereumjs-util/blob/75f529458bc7dc84f85fd0446d0fac92d991c262/index.js#L452-L466


#eip-6.md
### Title

      EIP: 6
      Title: Renaming SUICIDE opcode
      Author: Hudson Jameson <hudson@hudsonjameson.com>
      Status: Final
      Type: Standards Track
      Layer: Applications
      Created: 2015-11-22

### Abstract
The solution proposed in this EIP is to change the name of the `SUICIDE` opcode in Ethereum programming languages with `SELFDESTRUCT`.

### Motivation
Mental health is a very real issue for many people and small notions can make a difference. Those dealing with loss or depression would benefit from not seeing the word suicide in our a programming languages. By some estimates, 350 million people worldwide suffer from depression. The semantics of Ethereum's programming languages need to be reviewed often if we wish to grow our ecosystem to all types of developers.

An Ethereum security audit commissioned by DEVolution, GmbH and [performed by Least Authority](https://github.com/LeastAuthority/ethereum-analyses/blob/master/README.md) recommended the following:
> Replace the instruction name "suicide" with a less connotative word like "self-destruct", "destroy", "terminate", or "close", especially since that is a term describing the natural conclusion of a contract.

The primary reason for us to change the term suicide is to show that people matter more than code and Ethereum is a mature enough of a project to recognize the need for a change. Suicide is a heavy subject and we should make every effort possible to not affect those in our development community who suffer from depression or who have recently lost someone to suicide. Ethereum is a young platform and it will cause less headaches if we implement this change early on in it's life.

### Implementation
`SELFDESTRUCT` is added as an alias of `SUICIDE` opcode (rather than replacing it).
https://github.com/ethereum/solidity/commit/a8736b7b271dac117f15164cf4d2dfabcdd2c6fd
https://github.com/ethereum/serpent/commit/1106c3bdc8f1bd9ded58a452681788ff2e03ee7c


#eip-615.md
```
EIP: 615
Title: Subroutines and Static Jumps for the EVM
Status: Draft
Type: Core
Author: Greg Colvin <greg@colvin.org>, Paweł Bylica, Christian Reitwiessner
Created: 2016-12-10
Edited: 2017-25-4
```
## Abstract

This EIP introduces new EVM opcodes and conditions on EVM code to support subroutines and static jumps, disallow dynamic jumps, and thereby make EVM code amenable to linear-time static analysis.  This will provide for better compilation, interpretation, transpilation, and formal analysis of EVM code.

## MOTIVATION

All current implementations of the Ethereum Virtual Machine, including the just-in-time compilers, are much too slow. This proposal identifies a major reason for this and proposes changes to the EVM specification to address the problem.

In particular, it imposes restrictions on current EVM code and proposes new instructions to help provide for
* better-optimized compilation to native code
* faster interpretation
* faster transpilation to eWASM
* better compilation from other languages,
   including eWASM and Solidity
* better formal analysis tools

These goals are achieved by
* disallowing dynamic jumps
* introducing subroutines - jumps with return support
* disallowing pathological control flow and uses of the stack

We also propose to validate - in linear time - that EVM contracts correctly use subroutines, avoid misuse of the stack, and meet other safety conditions _before_ placing them on the blockchain.  Validated code precludes most runtime exceptions and the need to test for them.  And well-behaved control flow and use of the stack makes life easier for interpreters, compilers, formal analysis, and other tools.

## THE PROBLEM

Currently the EVM supports dynamic jumps, where the address to jump to is an argument on the stack. These dynamic jumps obscure the structure of the code and thus mostly inhibit control- and data-flow analysis.  This puts the quality and speed of optimized compilation fundamentally at odds.  Further, since every jump can potentially be to any jump destination in the code, the number of possible paths through the code goes up as the product of the number of jumps by the number of destinations, as does the time complexity of static analysis.  But absent dynamic jumps code can be statically analyzed in linear time.

Static analysis includes validation, and much of optimization, compilation, transpilation, and formal analysis; every part of the tool chain benefits when linear-time analysis is available.  In particular, faster control-flow analysis means faster compilation of EVM code to native code, and better data-flow analysis can help the compiler and the interpreter better track the size of the values on the stack and use native 64- and 32-bit operations when possible.  Also, conditions which are checked at validation time don’t have to be checked repeatedly at runtime.

Note that analyses of a contract’s bytecode before execution - such as optimizations performed before interpretation, JIT compilation, and on-the-fly machine code generation - must be efficient and linear-time. Otherwise, specially crafted contracts can be used as attack vectors against clients that use static analysis of EVM code before the creation or execution of contracts.

## PROPOSAL

We propose to deprecate two existing instructions - `JUMP` and `JUMPI`. They take their argument on the stack, which means that unless the value is constant they can jump to any `JUMPDEST`.  (In simple cases like `PUSH 0 JUMP` the value on the stack can be known to be constant, but in general it's difficult.)  We must nonetheless continue to support them in old code.

Having deprecated `JUMP` and `JUMPI`, we propose new instructions to support their legitimate uses.

### Preliminaries

These forms
* `INSTRUCTION x,`
* `INSTRUCTION x, y`
* `INSTRUCTION n, x ...`

name instructions with one, two, and two or more arguments, respectively.  An instruction is represented in the bytecode as a single-byte opcode.  The arguments are laid out as immediate data bytes following the opcode.  The size and encoding of immediate data fields is open to change.  In particular, easily-parsed variable-length encodings might prove useful for bytecode offsets - which are in practice small but in principle can be large.

### Primitives

The two most important uses of `JUMP` and `JUMPI` are static jumps and return jumps. Conditional and unconditional static jumps are the mainstay of control flow.  Return jumps are implemented as a dynamic jump to a return address pushed on the stack.  With the combination of a static jump and a dynamic return jump you can - and Solidity does - implement subroutines.  The problem is that static analysis cannot tell the one place the return jump is going, so it must analyze every possibility.

Static jumps are provided by
* `JUMPTO jump_target`
* `JUMPIF jump_target`
which are the same as `JUMP` and `JUMPI` except that they jump to an immediate `jump_target`, given as four immediate bytes, rather than an address on the stack.

To support subroutines, `BEGINSUB`, `JUMPSUB`, and `RETURNSUB` are provided.  Brief descriptions follow, and full semantics are given below.

* `BEGINSUB n_args, n_results`
marks the **single** entry to a subroutine.  `n_args` items are taken off of the stack at entry to, and `n_results` items are placed on the stack at return from the subroutine. `n_args` and `n_results` are given as one immediate byte each.  The bytecode for a subroutine ends at the next `BEGINSUB` instruction (or `BEGINDATA`, below) or at the end of the bytecode.

* `JUMPSUB jump_target`
jumps to an immediate subroutine address, given as four immediate bytes.

* `RETURNSUB`
returns from the current subroutine to the instruction following the JUMPSUB that entered it.

These five simple instructions form the primitives of the proposal.

### Data

In order to validate subroutines, EVM bytecode must be sequentially scanned matching jumps to their destinations.  Since creation code has to contain the runtime code as data, that code might not correctly validate in the creation context and also does not have to be validated prior to the execution of the creation code. Because of that, there needs to be a way to place data into the bytecode that will be skipped over and not validated.  Such data will prove useful for other purposes as well.

* `BEGINDATA`
specifies that all of the following bytes to the end of the bytecode are data, and not reachable code.

### Indirect Jumps

The primitive operations provide for static jumps.  Dynamic jumps are also used for O(1) indirection: an address to jump to is selected to push on the stack and be jumped to.  So we also propose two more instructions to provide for constrained indirection.  We support these with vectors of `JUMPDEST` or `BEGINSUB` offsets stored inline, which can be selected with an index on the stack.  That constrains validation to a specified subset of all possible destinations.  The danger of quadratic blow up is avoided because it takes as much space to store the jump vectors as it does to code the worst case exploit. 

Dynamic jumps to a `JUMPDEST` are used to implement O(1) jumptables, which are useful for dense switch statements, and are implemented as instructions similar to this one on most CPUs.
* `JUMPV n, jumpdest ...`
jumps to one of a vector of `n` `JUMPDEST` offsets via a zero-based index on the stack.  The vector is stored inline in the bytecode.  If the index is greater than or equal to `n - 1` the last (default) offset is used.  `n` is given as four immediate bytes, all `JUMPDEST` offsets as four immediate bytes each.

Dynamic jumps to a `BEGINSUB` are used to implement O(1) virtual functions and callbacks, which take just two pointer dereferences on most CPUs.
* `JUMPSUBV n, beginsub ...`
jumps to one of a vector of `n` `BEGINSUB` offsets via a zero-based index on the stack.  The vector is stored inline in the bytecode, MSB-first.  If the index is greater than or equal to `n - 1` the last (default) offset is used.  `n` is given as four immediate bytes, the `n` offsets as four immediate bytes each.

`JUMPV` and `JUMPSUBV` are not strictly necessary.  They provide O(1) operations that can be replaced by O(n) or O(log n) EVM code using static jumps, but that code will be slower, larger and use more gas for things that can and should be fast, small, and cheap, and that are directly supported in WASM with br_table and call_indirect.

### Variable Access

These operations provide convenient access to subroutine parameters and other variables at fixed stack offsets within a subroutine.

* `PUTLOCAL n`
Pops the top value on the stack and copies it to local variable `n`.

* `GETLOCAL n`
Pushes the value of local variable `n` on the EVM stack.

Local variable `n` is `FP[-n]` as defined below.

## SEMANTICS

Jumps to and returns from subroutines are described here in terms of
* the EVM data stack, (as defined in the [Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf) usually just called “the stack”,
* a return stack of `JUMPSUB` and `JUMPSUBV` offsets, and
* a frame stack of frame pointers.

We will adopt the following conventions to describe the machine state:
* The _program counter_ `PC` is (as usual) the byte offset of the currently executing instruction.
* The _stack pointer_ `SP` corresponds to the number of items on the stack - the _stack size_.  As a negative offset it addresses the current top of the stack of data values, where new items are pushed.
* The _frame pointer_ `FP` is set to `SP + n_args` at entry to the currently executing subroutine.
* The _stack items_ between the frame pointer and the current stack pointer are called the _frame_.
* The current number of items in the frame, `FP - SP`, is the _frame size_.

Defining the frame pointer so as to include the arguments is unconventional, but better fits our stack semantics and simplifies the remainder of the proposal.

The frame pointer and return stacks are internal to the subroutine mechanism, and not directly accessible to the program.  This is necessary to prevent the program from modifying its state in ways that could be invalid.

The first instruction of an array of EVM bytecode begins execution of a _main_ routine with no arguments, `SP` and `FP` set to 0, and with one value on the return stack - `code size - 1`. (Executing the virtual byte of 0 after this offset causes an EVM to stop.  Thus executing a `RETURNSUB` with no prior `JUMPSUB` or `JUMBSUBV` - that is, in the _main_ routine - executes a `STOP`.)

Execution of a subroutine begins with `JUMPSUB` or `JUMPSUBV`, which
* push `PC` on the return stack,
* push `FP` on the frame stack,
thus suspending execution of the current subroutine, and
* set `FP` to `SP + n_args`, and
* set `PC` to the specified `BEGINSUB` address,
thus beginning execution of the new subroutine.
(The _main_ routine is not addressable by `JUMPSUB` instructions.)

Execution of a subroutine is suspended during and resumed after execution of nested subroutines, and ends upon encountering a `RETURNSUB`, which
* sets `FP` to the top of the virtual frame stack and pops the stack, and
* sets `PC` to top of the return stack and pops the stack
* advances `PC` to the next instruction
thus resuming execution of the enclosing subroutine or _main_ program.
A `STOP or `RETURN` also ends the execution of a subroutine.

## VALIDITY

We would like to consider EVM code valid if and only if no execution of the program can lead to an exceptional halting state.  But we must and will validate code in linear time.  So our validation does not consider the code’s data and computations, only its control flow and stack use.  This means we will reject programs with invalid code paths, even if those paths cannot be executed at runtime.  Most conditions can be validated, and will not need to be checked at runtime; the exceptions are sufficient gas and sufficient stack.  So some false negatives and runtime checks are the price we pay for linear time validation.

_Execution_ is as defined in the Yellow Paper - a sequence of changes in the EVM state.  The conditions on valid code are preserved by state changes.  At runtime, if execution of an instruction would violate a condition the execution is in an exceptional halting state.  The yellow paper defines five such states.
>1  Insufficient gas

>2  More than 1024 stack items

>3  Insufficient stack items

>4  Invalid jump destination

>5  Invalid instruction

We propose to expand and extend the Yellow Paper conditions to handle the new instructions we propose. 

To handle the return stack we expand the conditions on stack size:
>2a  The size of the data stack does not exceed 1024.

>2b  The size of the return stack does not exceed 1024.

Given our more detailed description of the data stack we restate condition 3 - stack underflow - as
>3  `SP` must be less than or equal to `FP`

Since the various `DUP` and `SWAP` operations are formalized as taking items off the stack and putting them back on, this prevents `DUP` and `SWAP` from accessing data below the frame pointer, since taking too many items off of the stack would mean that `SP` is less than `FP`.

To handle the new jump instructions and subroutine boundaries we expand the conditions on jumps and jump destinations.
>4a  `JUMPTO`, `JUMPIF`, and `JUMPV` address only `JUMPDEST` instructions.

>4b  `JUMPSUB` and `JUMPSUBV` address only `BEGINSUB` instructions.

>4c  `JUMP` instructions do not address instructions outside of the subroutine they occur in.

We have two new conditions on execution to ensure consistent use of the stack by subroutines:
>6  For `JUMPSUB` and `JUMPSUBV` the frame size is at least the `n_args` of the `BEGINSUB`(s) to jump to.

>7  For `RETURNSUB` the frame size is equal to the `n_results` of the enclosing `BEGINSUB`.

Finally, we have one condition that prevents pathological uses of the stack:
>8  For every instruction in the code the frame size is constant.

In practice, we must test at runtime for conditions 1 and 2 - sufficient gas and sufficient stack.  We don’t know how much gas there will be, we don’t know how deep a recursion may go, and analysis of stack depth even for non-recursive programs is non-trivial.

All of the remaining conditions we validate statically.

## VALIDATION

Validation comprises two tasks:
* Checking that jump destinations are correct and instructions valid.
* Checking that subroutines satisfy the conditions on control flow and stack use.

We sketch out these two validation functions in pseudo-C below.   To simplify the presentation only the five primitives are handled (`JUMPV` and `JUMPSUBV` would just add more complexity to loop over their vectors), we assume helper functions for extracting instruction arguments from immediate data and managing the stack pointer and program counter, and some optimizations are forgone.

### Validating jumps

Validating that jumps are to valid addresses takes two sequential passes over the bytecode - one to build sets of jump destinations and subroutine entry points, another to check that addresses jumped to are in the appropriate sets.
```
    bytecode[code_size]   // contains EVM bytecode to validate
    is_sub[code_size]     // is there a BEGINSUB at PC?
    is_dest[code_size]    // is there a JUMPDEST at PC?
    sub_for_pc[code_size] // which BEGINSUB is PC in?
    
    bool validate_jumps(PC)
    {
        current_sub = PC

        // build sets of BEGINSUBs and JUMPDESTs
        for (PC = 0; instruction = bytecode[PC]; PC = advance_pc(PC))
        {
            if instruction is invalid
                return false
            if instruction is BEGINDATA
                return true
            if instruction is BEGINSUB
                is_sub[PC] = true
                current_sub = PC
                sub_for_pc[PC] = current_sub
            if instruction is JUMPDEST
                is_dest[PC] = true
            sub_for_pc[PC] = current_sub
        }
        
        // check that targets are in subroutine
        for (PC = 0; instruction = bytecode[PC]; PC = advance_pc(PC))
        {
            if instruction is BEGINDATA
                break;
            if instruction is BEGINSUB
                current_sub = PC
            if instruction is JUMPSUB
                if is_sub[jump_target(PC)] is false
                    return false
            if instruction is JUMPTO or JUMPIF
                if is_dest[jump_target(PC)] is false
                    return false
            if sub_for_pc[PC] is not current_sub
                return false
       }
        return true
    }
```
Note that code like this is already run by EVMs to check dynamic jumps, including building the jump destination set every time a contract is run, and doing a lookup in the jump destination set before every jump.

### Validating subroutines

This function can be seen as a symbolic execution of a subroutine in the EVM code, where only the effect of the instructions on the state being validated is computed.  Thus the structure of this function is very similar to an EVM interpreter.  This function can also be seen as an acyclic traversal of the directed graph formed by taking instructions as vertexes and sequential and branching connections as edges, checking conditions along the way.  The traversal is accomplished via recursion, and cycles are broken by returning when a vertex which has already been visited is reached.  The time complexity of this traversal is O(n-vertices + n-edges)

The basic approach is to call `validate_subroutine(i, 0, 0)`, for _i_ equal to the first instruction in the EVM code through each `BEGINDATA` offset.  `validate_subroutine()` traverses instructions sequentially, recursing when `JUMP` and `JUMPI` instructions are encountered.  When a destination is reached that has been visited before it returns, thus breaking cycles.  It returns true if the subroutine is valid, false otherwise.

```
    bytecode[code_size]     // contains EVM bytecode to validate
    frame_size[code_size ]  // is filled with -1

    // we validate each subroutine individually, as if at top level
    // * PC is the offset in the code to start validating at
    // * return_pc is the top PC on return stack that RETURNSUB returns to
    // * at top level FP = 0, so SP is both the frame size and the stack size
    validate_subroutine(PC, return_pc, SP)
    {
        // traverse code sequentially, recurse for jumps
        while true
        {
            instruction = bytecode[PC]

            // if frame size set we have been here before
            if frame_size[PC] >= 0
            {
                // check for constant frame size
                if instruction is JUMPDEST
                    if SP != frame_size[PC]
                        return false

                // return to break cycle
                return true
            }
            frame_size[PC] = SP

            // effect of instruction on stack
            n_removed = removed_items(instructions)
            n_added = added_items(instruction)

            // check for stack underflow
            if SP < n_removed
                return false

            // net effect of removing and adding stack items
            SP -= n_removed
            SP += n_added

            // check for stack overflow
            if SP > 1024
                return false

            if instruction is STOP, RETURN, SUICIDE or BEGINDATA
                return true	   

            // violates single entry
            if instruction is BEGINSUB
                 return false

            // return to top or from recursion to JUMPSUB
            if instruction is RETURNSUB
                break;

            if instruction is JUMPSUB
            {
                // check for enough arguments
                sub_pc = jump_target(PC)
                if SP < n_args(sub_pc)
                    return false
                return true
            }

            // reset PC to destination of jump
            if instruction is JUMPTO
            {
                PC = jump_target(PC)
                continue 
            }

            // recurse to jump to code to validate 
            if instruction is JUMPIF
            {
                if not validate_subroutine(jump_target(PC), return_pc, SP)
                    return false
            }

            // advance PC according to instruction
            PC = advance_pc(PC)
        }

        // check for right number of results
        if SP != n_results(return_pc)
            return false
        return true
    }
```

### COSTS & CODES

All of the instructions are O(1) with a small constant, requiring just a few machine operations each, whereas a `JUMP` or `JUMPI` must do an O(log n) binary search of an array of `JUMPDEST` offsets before every jump. With the cost of `JUMPI` being _high_ and the cost of `JUMP` being _mid_, we suggest the cost of `JUMPV` and `JUMPSUBV` should be _mid_, `JUMPSUB` and `JUMPIF` should be _low_, and`JUMPTO` should be _verylow_.  Measurement will tell.

We tentatively suggest the following opcodes:
```
0xB0 JUMPTO
0xB1 JUMPIF
0XB2 JUMPSUB
0xB4 JUMPSUBV
0xB5 BEGINSUB
0xB6 BEGINDATA
0xB8 RETURNSUB
0xB9 PUTLOCAL
0xBA GETLOCAL
```

### GETTING THERE FROM HERE

These changes would need to be implemented in phases at decent intervals:
>1 If this EIP is accepted, invalid code should be deprecated. Tools should stop generating invalid code, users should stop writing it, and clients should warn about loading it.

>2 A later hard fork would require clients to place only valid code on the block chain.  Note that despite the fork old EVM code will still need to be supported indefinitely.

If desired, the period of deprecation can be extended indefinitely by continuing to accept code not versioned as new - but without validation.  That is, by delaying step 2.  Since we must continue to run old code this is not technically difficult. 

Implementation of this proposal need not be difficult,  At the least, interpreters can simply be extended with the new opcodes and run unchanged otherwise.  The new opcodes require only stacks for the frame pointers and return offsets and the few pushes, pops, and assignments described above.  JIT code can use native calls.  Further optimizations include minimizing runtime checks for exceptions and taking advantage of validated code wherever possible.


#eip-7.md
### Title
      EIP: 7
      Title: DELEGATECALL
      Author: Vitalik Buterin <v@buterin.com>
      Status: Final
      Type: Homestead feature
      Created: 2015-11-15

### Overview

Add a new opcode, `DELEGATECALL` at `0xf4`, which is similar in idea to `CALLCODE`, except that it propagates the sender and value from the parent scope to the child scope, ie. the call created has the same sender and value as the original call.

### Specification

`DELEGATECALL`: `0xf4`, takes 6 operands:
- `gas`: the amount of gas the code may use in order to execute;
- `to`: the destination address whose code is to be executed;
- `in_offset`: the offset into memory of the input;
- `in_size`: the size of the input in bytes;
- `out_offset`: the offset into memory of the output;
- `out_size`: the size of the scratch pad for the output.

#### Notes on Gas
- The basic stipend is not given; `gas` is the total amount the callee receives.
- Like `CALLCODE`, account creation never happens, so the upfront gas cost is always `schedule.callGas` + `gas`.
- Unused gas is refunded as normal.

#### Notes on Sender
- `CALLER` and `VALUE` behave exactly in the callee's environment as they do in the caller's environment.

#### Other Notes
- The depth limit of 1024 is still preserved as normal.

### Rationale

Propagating the sender and value from the parent scope to the child scope makes it much easier for a contract to store another address as a mutable source of code and ''pass through'' calls to it, as the child code would execute in essentially the same environment (except for reduced gas and increased callstack depth) as the parent.

Use case 1: split code to get around 3m gas barrier

```python
~calldatacopy(0, 0, ~calldatasize())
if ~calldataload(0) < 2**253:
    ~delegate_call(msg.gas - 10000, $ADDR1, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
elif ~calldataload(0) < 2**253 * 2:
    ~delegate_call(msg.gas - 10000, $ADDR2, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
...
```

Use case 2: mutable address for storing the code of a contract:

```python
if ~calldataload(0) / 2**224 == 0x12345678 and self.owner == msg.sender:
    self.delegate = ~calldataload(4)
else:
    ~delegate_call(msg.gas - 10000, self.delegate, 0, ~calldatasize(), ~calldatasize(), 10000)
    ~return(~calldatasize(), 10000)
```
The child functions called by these methods can now freely reference `msg.sender` and `msg.value`.

### Possible arguments against

* You can replicate this functionality by just sticking the sender into the first twenty bytes of the call data. However, this would mean that code would need to be specially compiled for delegated contracts, and would not be usable in delegated and raw contexts at the same time.


#eip-8.md
### Title

      EIP: 8
      Title: devp2p Forward Compatibility Requirements for Homestead
      Author: Felix Lange <felix@ethdev.com>
      Status: Final
      Type: Standards Track
      Layer: Networking
      Created: 2015-12-18

### Abstract

This EIP introduces new forward-compatibility requirements for implementations of the
devp2p Wire Protocol, the RLPx Discovery Protocol and the RLPx TCP Transport Protocol.
Clients which implement EIP-8 behave according to Postel's Law:

> Be conservative in what you do, be liberal in what you accept from others.

### Specification

Implementations of **the devp2p Wire Protocol** should ignore the version number of hello
packets. When sending the hello packet, the version element should be set to the highest
devp2p version supported. Implementations should also ignore any additional list elements
at the end of the hello packet.

Similarly, implementations of **the RLPx Discovery Protocol** should not validate the
version number of the ping packet, ignore any additional list elements in any packet, and
ignore any data after the first RLP value in any packet. Discovery packets with unknown
packet type should be discarded silently. The maximum size of any discovery packet is
still 1280 bytes.

Finally, implementations of **the RLPx TCP Transport protocol** should accept a new
encoding for the encrypted key establishment handshake packets. If an EIP-8 style RLPx
`auth-packet` is received, the corresponding `ack-packet` should be sent using the rules
below.

Decoding the RLP data in `auth-body` and `ack-body` should ignore mismatches of `auth-vsn`
and `ack-vsn`, any additional list elements and any trailing data after the list. During
the transitioning period (i.e. until the old format has been retired), implementations
should pad `auth-body` with at least 100 bytes of junk data. Adding a random amount in
range [100, 300] is recommended to vary the size of the packet.

```text
auth-vsn         = 4
auth-size        = size of enc-auth-body, encoded as a big-endian 16-bit integer
auth-body        = rlp.list(sig, initiator-pubk, initiator-nonce, auth-vsn)
enc-auth-body    = ecies.encrypt(recipient-pubk, auth-body, auth-size)
auth-packet      = auth-size || enc-auth-body

ack-vsn          = 4
ack-size         = size of enc-ack-body, encoded as a big-endian 16-bit integer
ack-body         = rlp.list(recipient-ephemeral-pubk, recipient-nonce, ack-vsn)
enc-ack-body     = ecies.encrypt(initiator-pubk, ack-body, ack-size)
ack-packet       = ack-size || enc-ack-body

where

X || Y
    denotes concatenation of X and Y.
X[:N]
    denotes an N-byte prefix of X.
rlp.list(X, Y, Z, ...)
    denotes recursive encoding of [X, Y, Z, ...] as an RLP list.
sha3(MESSAGE)
    is the Keccak256 hash function as used by Ethereum.
ecies.encrypt(PUBKEY, MESSAGE, AUTHDATA)
    is the asymmetric authenticated encryption function as used by RLPx.
    AUTHDATA is authenticated data which is not part of the resulting ciphertext,
    but written to HMAC-256 before generating the message tag.
```

### Motivation

Changes to the devp2p protocols are hard to deploy because clients running an older
version will refuse communication if the version number or structure of the hello
(discovery ping, RLPx handshake) packet does not match local expectations.

Introducing forward-compatibility requirements as part of the Homestead consensus upgrade
will ensure that all client software in use on the Ethereum network can cope with future
network protocol upgrades (as long as backwards-compatibility is maintained).

### Rationale

The proposed changes address forward compatibility by applying Postel's Law (also known as
the Robustness Principle) throughout the protocol stack. The merit and applicability of
this approach has been studied repeatedly since its original application in RFC 761. For a
recent perspective, see
["The Robustness Principle Reconsidered" (Eric Allman, 2011)](http://queue.acm.org/detail.cfm?id=1999945).

#### Changes to the devp2p Wire Protocol

All clients currently contain statements such as the following:

```python
# pydevp2p/p2p_protocol.py
if data['version'] != proto.version:
    log.debug('incompatible network protocols', peer=proto.peer,
        expected=proto.version, received=data['version'])
    return proto.send_disconnect(reason=reasons.incompatibel_p2p_version)
```

These checks make it impossible to change the version or structure of the hello packet.
Dropping them enables switching to a newer protocol version: Clients implementing a newer
version simply send a packet with higher version and possibly additional list elements.

* If such a packet is received by a node with lower version, it will blindly assume that
  the remote end is backwards-compatible and respond with the old handshake.
* If the packet is received by a node with equal version, new features of the protocol can
  be used.
* If the packet is received by a node with higher version, it can enable
  backwards-compatibility logic or drop the connection.

#### Changes to the RLPx Discovery Protocol

The relaxation of discovery packet decoding rules largely codifies current practice. Most
existing implementations do not care about the number of list elements (an exception being
go-ethereum) and do not reject nodes with mismatching version. This behaviour is not
guaranteed by the spec, though.

If adopted, the change makes it possible to deploy protocol changes in a similar manner to
the devp2p hello change: simply bump the version and send additional information. Older
clients will ignore the additional elements and can continue to operate even when the
majority of the network has moved on to a newer protocol.

#### Changes to the RLPx TCP Handshake

Discussions of the RLPx v5 changes (chunked packets, change to key derivation) have
faltered in part because the v4 handshake encoding provides only one in-band way to add a
version number: shortening the random portion of the nonce. Even if the RLPx v5 handshake
proposal were accepted, future upgrades are hard because the handshake packet is a fixed
size ECIES ciphertext with known layout.

I propose the following changes to the handshake packets:

* Adding the length of the ciphertext as a plaintext header.
* Encoding the body of the handshake as RLP.
* Adding a version number to both packets in place of the token flag (unused).
* Removing the hash of the ephemeral public key (it is redundant).

These changes make it possible to upgrade the RLPx TCP transport protocol in the same
manner as described for the other protocols, i.e. by adding list elements and bumping the
version. Since this is the first change to the RLPx handshake packet, we can seize the
opportunity to remove all currently unused fields.

Additional data is permitted (and in fact required) after the RLP list because the
handshake packet needs to grow in order to be distinguishable from the old format.
Clients can employ logic such as the following pseudocode to handle both formats
simultaneously.

```go
packet = read(307, connection)
if decrypt(packet) {
    // process as old format
} else {
    size = unpack_16bit_big_endian(packet)
    packet += read(size - 307 + 2, connection)
    if !decrypt(packet) {
        // error
    }
    // process as new format
}
```

The plain text size prefix is perhaps the most controversial aspect of this document. It
has been argued that the prefix aids adversaries that seek to filter and identify RLPx
connections on the network level.

This is largely a question of how much effort the adversary is willing to expense. If the
recommendation to randomise the lengths is followed, pure pattern-based packet
recognition is unlikely to succeed.

* For typical firewall operators, blocking all connections whose first two bytes form an
  integer in range [300,600] is probably too invasive. Port-based blocking would be
  a more effective measure to filter most RLPx traffic.
* For an attacker who can afford to correlate many criteria, the size prefix would ease
  recognition because it adds to the indicator set. However, such an attacker could also
  be expected to read or participate in RLPx Discovery traffic, which would be sufficient
  to enable blocking of RLPx TCP connections whatever their format is.

### Backwards Compatibility

This EIP is backwards-compatible, all valid version 4 packets are still accepted.

### Implementation

[go-ethereum](https://github.com/ethereum/go-ethereum/pull/2091)
[libweb3core](https://github.com/ethereum/libweb3core/pull/46)
[pydevp2p](https://github.com/ethereum/pydevp2p/pull/32)

### Test Vectors

#### devp2p Base Protocol

devp2p hello packet advertising version 22 and containing a few additional list elements:

```text
f87137916b6e6574682f76302e39312f706c616e39cdc5836574683dc6846d6f726b1682270fb840
fda1cff674c90c9a197539fe3dfb53086ace64f83ed7c6eabec741f7f381cc803e52ab2cd55d5569
bce4347107a310dfd5f88a010cd2ffd1005ca406f1842877c883666f6f836261720304
```

#### RLPx Discovery Protocol

Implementations should accept the following encoded discovery packets as valid.
The packets are signed using the secp256k1 node key

```text
b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291
```

ping packet with version 4, additional list elements:

```text
e9614ccfd9fc3e74360018522d30e1419a143407ffcce748de3e22116b7e8dc92ff74788c0b6663a
aa3d67d641936511c8f8d6ad8698b820a7cf9e1be7155e9a241f556658c55428ec0563514365799a
4be2be5a685a80971ddcfa80cb422cdd0101ec04cb847f000001820cfa8215a8d790000000000000
000000000000000000018208ae820d058443b9a3550102
```

ping packet with version 555, additional list elements and additional random data:

```text
577be4349c4dd26768081f58de4c6f375a7a22f3f7adda654d1428637412c3d7fe917cadc56d4e5e
7ffae1dbe3efffb9849feb71b262de37977e7c7a44e677295680e9e38ab26bee2fcbae207fba3ff3
d74069a50b902a82c9903ed37cc993c50001f83e82022bd79020010db83c4d001500000000abcdef
12820cfa8215a8d79020010db885a308d313198a2e037073488208ae82823a8443b9a355c5010203
040531b9019afde696e582a78fa8d95ea13ce3297d4afb8ba6433e4154caa5ac6431af1b80ba7602
3fa4090c408f6b4bc3701562c031041d4702971d102c9ab7fa5eed4cd6bab8f7af956f7d565ee191
7084a95398b6a21eac920fe3dd1345ec0a7ef39367ee69ddf092cbfe5b93e5e568ebc491983c09c7
6d922dc3
```

pong packet with additional list elements and additional random data:

```text
09b2428d83348d27cdf7064ad9024f526cebc19e4958f0fdad87c15eb598dd61d08423e0bf66b206
9869e1724125f820d851c136684082774f870e614d95a2855d000f05d1648b2d5945470bc187c2d2
216fbe870f43ed0909009882e176a46b0102f846d79020010db885a308d313198a2e037073488208
ae82823aa0fbc914b16819237dcd8801d7e53f69e9719adecb3cc0e790c57e91ca4461c9548443b9
a355c6010203c2040506a0c969a58f6f9095004c0177a6b47f451530cab38966a25cca5cb58f0555
42124e
```

findnode packet with additional list elements and additional random data:

```text
c7c44041b9f7c7e41934417ebac9a8e1a4c6298f74553f2fcfdcae6ed6fe53163eb3d2b52e39fe91
831b8a927bf4fc222c3902202027e5e9eb812195f95d20061ef5cd31d502e47ecb61183f74a504fe
04c51e73df81f25c4d506b26db4517490103f84eb840ca634cae0d49acb401d8a4c6b6fe8c55b70d
115bf400769cc1400f3258cd31387574077f301b421bc84df7266c44e9e6d569fc56be0081290476
7bf5ccd1fc7f8443b9a35582999983999999280dc62cc8255c73471e0a61da0c89acdc0e035e260a
dd7fc0c04ad9ebf3919644c91cb247affc82b69bd2ca235c71eab8e49737c937a2c396
```

neighbours packet with additional list elements and additional random data:

```text
c679fc8fe0b8b12f06577f2e802d34f6fa257e6137a995f6f4cbfc9ee50ed3710faf6e66f932c4c8
d81d64343f429651328758b47d3dbc02c4042f0fff6946a50f4a49037a72bb550f3a7872363a83e1
b9ee6469856c24eb4ef80b7535bcf99c0004f9015bf90150f84d846321163782115c82115db84031
55e1427f85f10a5c9a7755877748041af1bcd8d474ec065eb33df57a97babf54bfd2103575fa8291
15d224c523596b401065a97f74010610fce76382c0bf32f84984010203040101b840312c55512422
cf9b8a4097e9a6ad79402e87a15ae909a4bfefa22398f03d20951933beea1e4dfa6f968212385e82
9f04c2d314fc2d4e255e0d3bc08792b069dbf8599020010db83c4d001500000000abcdef12820d05
820d05b84038643200b172dcfef857492156971f0e6aa2c538d8b74010f8e140811d53b98c765dd2
d96126051913f44582e8c199ad7c6d6819e9a56483f637feaac9448aacf8599020010db885a308d3
13198a2e037073488203e78203e8b8408dcab8618c3253b558d459da53bd8fa68935a719aff8b811
197101a4b2b47dd2d47295286fc00cc081bb542d760717d1bdd6bec2c37cd72eca367d6dd3b9df73
8443b9a355010203b525a138aa34383fec3d2719a0
```

#### RLPx Handshake

In these test vectors, node A initiates a connection with node B.
The values contained in all packets are given below:

```text
Static Key A:    49a7b37aa6f6645917e7b807e9d1c00d4fa71f18343b0d4122a4d2df64dd6fee
Static Key B:    b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291
Ephemeral Key A: 869d6ecf5211f1cc60418a13b9d870b22959d0c16f02bec714c960dd2298a32d
Ephemeral Key B: e238eb8e04fee6511ab04c6dd3c89ce097b11f25d584863ac2b6d5b35b1847e4
Nonce A:         7e968bba13b6c50e2c4cd7f241cc0d64d1ac25c7f5952df231ac6a2bda8ee5d6
Nonce B:         559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd
```

(Auth₁)  RLPx v4 format (sent from A to B):
```text
048ca79ad18e4b0659fab4853fe5bc58eb83992980f4c9cc147d2aa31532efd29a3d3dc6a3d89eaf
913150cfc777ce0ce4af2758bf4810235f6e6ceccfee1acc6b22c005e9e3a49d6448610a58e98744
ba3ac0399e82692d67c1f58849050b3024e21a52c9d3b01d871ff5f210817912773e610443a9ef14
2e91cdba0bd77b5fdf0769b05671fc35f83d83e4d3b0b000c6b2a1b1bba89e0fc51bf4e460df3105
c444f14be226458940d6061c296350937ffd5e3acaceeaaefd3c6f74be8e23e0f45163cc7ebd7622
0f0128410fd05250273156d548a414444ae2f7dea4dfca2d43c057adb701a715bf59f6fb66b2d1d2
0f2c703f851cbf5ac47396d9ca65b6260bd141ac4d53e2de585a73d1750780db4c9ee4cd4d225173
a4592ee77e2bd94d0be3691f3b406f9bba9b591fc63facc016bfa8
```

(Auth₂) EIP-8 format with version 4 and no additional list elements (sent from A to B):
```text
01b304ab7578555167be8154d5cc456f567d5ba302662433674222360f08d5f1534499d3678b513b
0fca474f3a514b18e75683032eb63fccb16c156dc6eb2c0b1593f0d84ac74f6e475f1b8d56116b84
9634a8c458705bf83a626ea0384d4d7341aae591fae42ce6bd5c850bfe0b999a694a49bbbaf3ef6c
da61110601d3b4c02ab6c30437257a6e0117792631a4b47c1d52fc0f8f89caadeb7d02770bf999cc
147d2df3b62e1ffb2c9d8c125a3984865356266bca11ce7d3a688663a51d82defaa8aad69da39ab6
d5470e81ec5f2a7a47fb865ff7cca21516f9299a07b1bc63ba56c7a1a892112841ca44b6e0034dee
70c9adabc15d76a54f443593fafdc3b27af8059703f88928e199cb122362a4b35f62386da7caad09
c001edaeb5f8a06d2b26fb6cb93c52a9fca51853b68193916982358fe1e5369e249875bb8d0d0ec3
6f917bc5e1eafd5896d46bd61ff23f1a863a8a8dcd54c7b109b771c8e61ec9c8908c733c0263440e
2aa067241aaa433f0bb053c7b31a838504b148f570c0ad62837129e547678c5190341e4f1693956c
3bf7678318e2d5b5340c9e488eefea198576344afbdf66db5f51204a6961a63ce072c8926c
```

(Auth₃) EIP-8 format with version 56 and 3 additional list elements (sent from A to B):
```text
01b8044c6c312173685d1edd268aa95e1d495474c6959bcdd10067ba4c9013df9e40ff45f5bfd6f7
2471f93a91b493f8e00abc4b80f682973de715d77ba3a005a242eb

#new_light_client_protocol.md

### Summary

The [blockhash refactoring EIP](http://github.com/ethereum/EIPs/pull/210) allows blocks to directly link to blocks much older than themselves, making all blocks in the chain relatively tightly connected to each other. This allows for very efficient light client proofs that do not require light clients to verify an entire header chain; instead, light clients can verify a subchain containing "key blocks" whose ethash mining result hits an especially low target, and gain a probabilistic assurance that the longest chain contains these key blocks.

### Proof format

We can define a "probabilistic total-difficulty proof" as an RLP list as follows:

    [header1, proof1, header2, proof2, ...]
    
Where each header is a block header, and each proof[i] is a Merkle branch from header[i] to the hash of header[i + 1]. More formally, the proof is an RLP list where each element contains as a substring the hash of the next element, and the last element is the hash of the next header; the elements are taken from the branch of the state tree in header[i] that points to the hash of header[i + 1] that is available in the storage of the BLOCKHASH_CONTRACT_ADDR.

The proof serves to verify that the headers are linked to each other in the given order, and that the given chain has an approximate total difficulty equal to `sum(2 ** 256 / mining_result[i])` where `mining_result[i]` is the result of running the ethash verification function on the given header. A node producing a proof will take case to create a proof that contains as many low-mining-result blocks as possible; a specific algorithm would be to look for all "key blocks" whose mining result is less than 1/50000 of maximum for a valid block allowed by the most recent block difficulty, and then if these blocks do not have a direct connection because they are not an even multiple of 256 or 65536 apart, it would find "glue blocks" to link between them; for example, linking 3904322 to 3712498 might go through 3735552 (multiple of 65536, directly linked in 3904322) and 3712512 (multiple of 256, directly linked in 3735552), and finally 3712512 links directly to 3712498.

### Light client algorithm

Suppose that a light client receives a proof as above. The light client can try to answer this question: suppose that there is an attacker with the same amount of hashpower as the main chain. Given some probability threshold p (say, 1 in 1 million), how many blocks would the main chain be able to grow with probability 1-p in the same amount of time that the attacker makes their proof?

For example, let's suppose that we have a proof 8 blocks long, with mining results `[8937, 3047, 2601, 1612, 273, 3278, 1220, 1942]` (in a real-world example, all of these numbers would of course be very large values somewhere around 2**200). We can set up a thought experiment where an attacker and the "main chain" create blocks in parallel; the question asked is, what is the number TD such that while the main chain creates a number of blocks with the given total difficulty TD, the attacker can come up with at least 8 blocks with mining result less than or equal to 8937? The answer comes from the Poisson distribution's cumulative distribution function formula; the answer is, enough TD to create 81 blocks of mining result less than 1 million. Note that this carries high inefficiency: the simulation that actually gave that output involved 800 blocks of mining result less than 1 million. We can alleviate this problem by choosing a higher proof length, say 56; this would get us to the point where we cross the threshold at N = 400.

Now, we can get to our algorithm. A light client starts off knowing the genesis, and asks for probabilistic total-difficulty proofs. It stores a map `height_diffs: {(block_hash_from, block_hash_to): min length}`, which starts off as `{genesis: 0}`. When it receives a proof, it sets `height_diffs[(LAST_BLOCK, FIRST_BLOCK)] = max(height_diffs[(LAST_BLOCK, FIRST_BLOCK)], min_length(PROOF))`, where `min_length` is a function that computes the min length as above. Then, at any point the algorithm can find a min-height of any given block by applying any pathfinding algorithm ([Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) is ideal) to get the total min-length from the genesis to that block. The block with the highest min-height is taken to be the head.

Note that it is expected that proofs for the portion of the chain further back in the tail will be more "rarefied", including only perhaps one block per 20000 heights, but closer to the head the proofs will become "tighter", as there will be fewer blocks between the start of the proof and the head, and so the distance between successive blocks would need to be smaller for the proof to still contain enough blocks to have a reasonably high min-length. Once a client asks for proofs starting from a header that is less than ~250 blocks from the head, it may become reasonable to simply give it the entire sub-chain, ie. `[header[n], header[n+1], ... , header[n + 250]]`; the light client can interpret a sub-chain as a proof with a min-length that is simply equal to the total difficulty of the sub-chain.

### Estimated complexity

Suppose that there are 1 million blocks between the genesis (actually, we can use the Metropolis hardfork block as a "genesis", as this algorithm does not work before the hard fork anyway) and the head. Suppose that a client wants to be secure against attackers with up to half the hashpower of the main network with p = 0.999999. Then, the client would want to ensure that *any* subchain from the genesis to the head has a min-length of at least half its claimed length. We already roughly know from above that it takes 64 headers to get to that level. As an approximation, the client can ask for such a subchain for blocks 0....500000, then 500000...750000, and so forth. At 999750, it can stop, and simply take 250 block headers. In total, this would entail 12 proofs (768 headers), plus 768 Merkle branches, plus another 250 headers. A branch on average takes ~1000 bytes, a header takes ~500 bytes, so this would be ~1.27 MB, and would require 1018 ethash verifications from 30 epochs (so an additional 30 cache generations).


