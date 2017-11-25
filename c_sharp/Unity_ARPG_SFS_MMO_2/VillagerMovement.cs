using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VillagerMovement : MonoBehaviour {

	public float moveSpeed;
	private Vector2 minWalkPoint;
	private Vector2 maxWalkPoint;
	private bool hasWalkZone;

	private Rigidbody2D myRigidBody;

	public bool isWalking;

	public float walkTime;
	private float walkCounter;
	public float waitTime;
	private float waitCounter;

	private int WalkDirection;

    public bool canMove;
    private DialogueManager theDM;

	public Collider2D walkZone;

	// Use this for initialization
	void Start () {
		myRigidBody = GetComponent<Rigidbody2D> ();
        theDM = FindObjectOfType<DialogueManager>();

		waitCounter = waitTime;
		walkCounter = walkTime;

		ChooseDirection ();

		if (walkZone != null) 
		{
			minWalkPoint = walkZone.bounds.min;
			maxWalkPoint = walkZone.bounds.max;
			hasWalkZone = true;
		}

        canMove = true;
	}
	
	// Update is called once per frame
	void Update () {

        if (!theDM.dialogueActive)
        {
            canMove = true;
        }

        if (!canMove)
        {
            myRigidBody.velocity = Vector2.zero;
            return;
        }

		if (isWalking) 
		{
			
			switch (WalkDirection) 
			{
			case 0:
				myRigidBody.velocity = new Vector2 (0, moveSpeed);
				if (hasWalkZone && transform.position.y >= maxWalkPoint.y) 
				{
					isWalking = false;
					waitCounter = waitTime;
				}
				break;
			case 1:
				myRigidBody.velocity = new Vector2 (moveSpeed, 0);
				if (hasWalkZone && transform.position.x >= maxWalkPoint.x) 
				{
					isWalking = false;
					waitCounter = waitTime;
				}
				break;

			case 2:
				myRigidBody.velocity = new Vector2 (0, -moveSpeed);
				if (hasWalkZone && transform.position.y <= minWalkPoint.y) 
				{
					isWalking = false;
					waitCounter = waitTime;
				}
				break;

			case 3:
				myRigidBody.velocity = new Vector2 (-moveSpeed, 0);
				if (hasWalkZone && transform.position.x <= minWalkPoint.x) 
				{
					isWalking = false;
					waitCounter = waitTime;
				}
				break;
			}

			walkCounter -= Time.deltaTime;

			if (walkCounter < 0) 
			{
				isWalking = false;
				waitCounter = waitTime;
			}

		} else 
		{
			waitCounter -= Time.deltaTime;

			myRigidBody.velocity = Vector2.zero;

			if (waitCounter < 0) 
			{
				ChooseDirection ();
			}
		}
	}

	public void ChooseDirection()
	{
		WalkDirection = Random.Range (0, 4);
		isWalking = true;
		walkCounter = walkTime;
	}
}
