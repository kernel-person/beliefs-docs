# Adoption

Adoption connects a child to the agreed parent group. Marriage does not add or remove parents automatically.

## Request adoption

1. Run `/faith relationships`.
2. Choose **Adopt as my child** and select a nearby player, or **Ask to be adopted** and choose your proposed parent.
3. Review the full list. Selecting a married parent includes **every member of their current marriage group**. An unmarried parent is listed alone.
4. Choose **Send request**. Your consent is recorded; every other parent and the child must each open the request and choose **Accept adoption**. Requests are also available through `/faith pending`.
5. Open **Priest help → Ask for help** if you need compatible clergy. The priest must not be a parent or the child in this request.
6. Gather with that priest, online and alive in the same world. By default, all participants must be within **32 blocks**. The priest completes the adoption after everyone has consented.

The completed connection appears in your [family tree](family-tree.md). Divorce and changes of faith do not remove it. A future marriage does not automatically add new parents.

??? tip "The request cannot complete"

    The child must have no active parent connections. Nobody can become their own parent, create an ancestry loop or make an existing marriage join relatives. A changed parent group needs a fresh review and request. Requests expire after 5 minutes by default; the server can change this limit.

??? info "Cancel before completion"

    Use **Decline** or **Cancel request** in the pending request. This cancels the proposal. It does not undo a completed adoption. **Priest help** only coordinates a meeting; volunteering never supplies anyone's consent.

## End an adoption connection

Open `/faith relationships` → **End adoption**, choose the parent or child, then confirm. `/faith unadopt [player]` opens the same review.

Either person can end their direct connection. Other parents remain. Once all active parent connections have ended, the child can be adopted again.

The ended link leaves the family tree, but its ancestry stays recorded for safeguards. Former relatives still cannot marry, and a new adoption cannot create a cycle or make an existing marriage join relatives.

For partner groups and their separate rules, read [Marriage](marriage.md).
