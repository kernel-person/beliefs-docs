# Adoption

Adoption connects a child to the agreed parent group. Marriage does not add or remove parents automatically.

## Request adoption

1. Run `/faith relationships`.
2. Choose **Adopt as my child** and select a nearby player, or **Ask to be adopted** and choose your proposed parent.
3. Review the full list. Selecting a married parent includes **every member of their current marriage group**. An unmarried parent is listed alone.
4. Choose **Send request**. Your consent is recorded; every other parent and the child must each open the request and choose **Accept adoption**. Requests are also available through `/faith pending`.
5. Adoption completes as soon as everyone accepts. No priest or gathering is needed.

The completed connection appears in your [family tree](family-tree.md). Divorce and changes of faith do not remove it. A future marriage does not automatically add new parents.

## Make it a ceremony

Choose **Plan ceremony** before sending the request. Everyone accepts, then a compatible priest who is not a parent or the child completes it with everyone nearby. The default range is **32 blocks** in the same world. Use **Priest help** from that request to arrange the meeting. Older requests retain their ceremony requirement.

??? tip "The request cannot complete"

    The child must have no active parent connections. Nobody can become their own parent, create an ancestry loop or make an existing marriage join relatives. A changed parent group needs a fresh review and request. Requests expire after 5 minutes by default; the server can change this limit.

??? info "Cancel before completion"

    Use **Decline** or **Cancel request** in the pending request. This cancels the proposal. It does not undo a completed adoption. For ceremony requests, **Priest help** coordinates a meeting; volunteering never supplies anyone's consent.

## End an adoption connection

Open `/faith relationships` → **End adoption**, choose the parent or child, then confirm. `/faith unadopt [player]` opens the same review.

Either person can end their direct connection. Other parents remain. Once all active parent connections have ended, the child can be adopted again.

The ended link leaves the family tree, but its ancestry stays recorded for safeguards. Former relatives still cannot marry, and a new adoption cannot create a cycle or make an existing marriage join relatives.

For partner groups and their separate rules, read [Marriage](marriage.md).
